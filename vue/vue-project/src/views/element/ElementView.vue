<template>
  <div>
    <el-upload
      class="upload-demo"
      drag
      action="https://jsonplaceholder.typicode.com/posts/"
      multiple
    >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">
        只能上传jpg/png文件，且不超过500kb
      </div>
    </el-upload>
    <el-row>
        <!-- <el-button>默认按钮</el-button> -->
        <el-button type="primary">取消</el-button>
        <el-button type="success">确认</el-button>
        <!-- <el-button type="info">信息按钮</el-button>
        <el-button type="warning">警告按钮</el-button>
        <el-button type="danger">危险按钮</el-button> -->
        </el-row> 
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>