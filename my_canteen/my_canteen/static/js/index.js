new Vue({
  el: '#app',
  data: function() {
    return {
      visible: false,
      activeName: 'first',
      dialogVisible: false,
      activeIndex2: '1',
      input1: '',
      tableData: [{
        id: '1',
        name: '王小虎',
        age: '29',
        phone: '18801111222',
        role: '员工',
        certificate: '有',
        education: '本科',
      },{
        id: '1',
        name: '王小虎',
        age: '29',
        phone: '18801111222',
        role: '员工',
        certificate: '有',
        education: '本科',
      },{
        id: '1',
        name: '王小虎',
        age: '29',
        phone: '18801111222',
        role: '员工',
        certificate: '有',
        education: '本科',
      },{
        id: '1',
        name: '王小虎',
        age: '29',
        phone: '18801111222',
        role: '员工',
        certificate: '有',
        education: '本科',
      }]
    }
  },
  mounted () {
  },
  methods: {
    handleSelect () {
    },
    handleClick () {
    },
    handleClose () {
    },
    saveForm() {
      console.log(this)
      this.$confirm('确认保存修改吗, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '保存成功!'
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消保存'
        });
      });
    }
  }
})