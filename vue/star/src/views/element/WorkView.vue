<template>
  <el-container class="upload-container">
    <el-main>
      <div class="container">
        <el-upload
          class="upload-demo"
          ref="upload"
          action="http://127.0.0.1:5000/upload"
          multiple
          :on-success="handleAvatarSuccess"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :file-list="fileList"
          :auto-upload="false"
        >
          <el-button slot="trigger" size="small" type="primary"
            >选取文件</el-button
          >
          <el-button
            style="margin-left: 10px"
            size="small"
            type="success"
            @click="submitUpload"
            >上传变化前图片</el-button
          >
          <el-button style="margin-left: 10px" size="small" type="primary"
            ><router-link to="/work" class="no">下一步</router-link></el-button
          >
          <el-button style="margin-left: 10px" size="small" type="primary"
            ><router-link to="/" class="no"
              >返回上一个界面</router-link
            ></el-button
          >
          <div slot="tip" class="el-upload__tip">
            只能上传一个bmp文件，且不超过500kb
          </div>
        </el-upload>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      fileList: [],
    };
  },
  methods: {
    handleAvatarSuccess() {},
    submitUpload() {
      this.$refs.upload.submit();
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
  },
};
</script>

<style>
.no {
  text-decoration: none;
  color: white;
}

.el-button {
  margin-right: 10px;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.centered {
  text-align: center;
}
.upload-container {
  background-color: #f2f2f2;
  padding: 20px;
  border: 1px solid #ccc;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>