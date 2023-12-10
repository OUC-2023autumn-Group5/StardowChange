<template>
<div class="image__preview">
  <div style="display: flex;justify-content: center;align-items: center;"><el-button style="margin-left: 10px;" size="small" type="primary"><router-link to="/" class="no">返回初始界面</router-link></el-button></div>
  <div class="container"><el-image 
    style="width: 650px; height: 650px"
    :src="url" >
  </el-image>
  </div>
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
    margin-top: 30px;
  }
  .container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90vh;
}
</style>