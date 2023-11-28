
<template>
 
<div>
  <el-upload
  class="upload-demo"
  ref="upload"
  action="http://localhost:5000/upload"
  :on-success="handleAvatarSuccess"
  :on-preview="handlePreview"
  :on-remove="handleRemove"
  :file-list="fileList"
  :auto-upload="false">
  <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
  <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload"><router-link to="/result" class="no">查看结果</router-link></el-button>
  <el-button style="margin-left: 10px;" size="small" type="primary" ><router-link to="/" class="no">返回上一个界面</router-link></el-button>
  <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
</el-upload>

</div>

</template>
<script>
  export default {
    data() {
      return {
        fileList: [],
      };
    },
    methods: {
      handleAvatarSuccess() {

      },
      submitUpload() {
        this.$refs.upload.submit();
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePreview(file) {
        console.log(file);
      }
    }
  }
  
</script>

<style >
  .no {
    text-decoration:none;
    color: white;
  }

</style>