<template>
<div class="image__preview">
  <div><el-button style="margin-left: 10px;" size="small" type="primary" ><router-link to="/" class="no">返回初始界面</router-link></el-button></div>
  <el-image 
    style="width: 500px; height: 500px"
    :src="url" >
  </el-image>
</div>
</template>

<script>
  export default {
    data() {
      return {
        url: 'result.png',
      };
    },
    methods: {
      
    }
  }
  
</script>

<style >
 .image__preview{
    margin-top: 50px;
  }
</style>