
/*==============================================================*/
/* Table: canteen                                               */
/*==============================================================*/
create table canteen
(
   canteen_id           int not null auto_increment,
   canteen_name         varchar(10) not null,
   canteen_campus         varchar(20) not null,
   canteen_photo        longblob not null,
   sanitation_level     char(1) not null,
   canteen_active       bool not null,
   primary key (canteen_id)
);


/*==============================================================*/
/* Table: customer                                              */
/*==============================================================*/
create table customer
(
   customer_id          int not null auto_increment,
   customer_name        varchar(20) not null,
   cusomer_password     varchar(20),
   studentID            varchar(20) not null,
   campus               varchar(20) not null,
   customer_tel         numeric(11,0) not null,
   customer_status      int not null,
   create_time          datetime not null,
   primary key (customer_id)
);

/*==============================================================*/
/* Table: dish                                                  */
/*==============================================================*/
create table dish
(
   dish_id              int not null auto_increment,
   shop_id              int not null,
   dish_name            varchar(20) not null,
   dish_detail          longtext not null,
   dish_price           real not null,
   dish_photo           longblob not null,
   dish_active          bool not null,
   primary key (dish_id)
);

/*==============================================================*/
/* Index: idx_dish_name                                         */
/*==============================================================*/
create index idx_dish_name on dish
(
   dish_name
);

/*==============================================================*/
/* Table: orders                                                */
/*==============================================================*/
create table orders
(
   order_id             int not null auto_increment,
   dish_id              int not null,
   customer_id          int not null,
   order_price          real not null,
   order_status         varchar(10) not null default '已下单',
   order_time           datetime not null,
   table_numbers        varchar(20),
   dish_quantity        int,
   evaluation_status    int,
   eva_content          varchar(255),
   primary key (order_id)
);

/*==============================================================*/
/* Table: shop                                                  */
/*==============================================================*/
create table shop
(
   shop_id              int not null auto_increment,
   canteen_id           int not null,
   manager_id           int not null,
   shop_name            varchar(20) not null,
   shop_detail          longtext not null,
   shop_photo           longblob not null,
   shop_active          bool not null,
   primary key (shop_id)
);

/*==============================================================*/
/* Table: shop_manager                                          */
/*==============================================================*/
create table shop_manager
(
   manager_id           int not null auto_increment,
   manager_name         varchar(20) not null,
   manager_password     varchar(20),
   manage_shop_sum      int not null,
   Tel_number           numeric(11,0) not null,
   manage_tel           varchar(20) not null,
   manager_status       int not null,
   primary key (manager_id)
);

/*==============================================================*/
/* View: viewDishHot                                            */
/*==============================================================*/
create  VIEW      viewDishHot
  as
select dish.dish_id, dish_name, count(*) as hot, avg(comment_score) as avg_score
from dish, orders, comments
where dish.dish_id = orders.dish_id and
      comments.order_id = orders.order_id
group by dish_id
order by count(*) desc;

alter table comments add constraint FK_order_comment foreign key (order_id)
      references orders (order_id) on delete restrict on update restrict;

alter table dish add constraint FK_shop_dish foreign key (shop_id)
      references shop (shop_id) on delete restrict on update restrict;

alter table orders add constraint FK_customer_order foreign key (customer_id)
      references customer (customer_id) on delete restrict on update restrict;

alter table orders add constraint FK_dish_order foreign key (dish_id)
      references dish (dish_id) on delete restrict on update restrict;

alter table shop add constraint FK_canteen_shop foreign key (canteen_id)
      references canteen (canteen_id) on delete restrict on update restrict;

alter table shop add constraint FK_manager_shop foreign key (manager_id)
      references shop_manager (manager_id) on delete restrict on update restrict;


CREATE TRIGGER GetTime_BEFORE_INSERT_COMMENT
 BEFORE INSERT ON comments
 FOR EACH ROW
 SET NEW.comment_time = NOW();


CREATE TRIGGER GetTime_BEFORE_INSERT_ORDER
 BEFORE INSERT ON orders
 FOR EACH ROW
 SET NEW.order_time = NOW();