<template>
  <div class="container">
    <el-container>
      <el-main>
        <div class="centered">
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
            <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
            <el-button size="small" type="success" @click="submitUpload">上传变化前图片</el-button>
            <el-button size="small" type="primary"><router-link to="/work" class="no">下一步</router-link></el-button>
            <el-button size="small" type="primary"><router-link to="/" class="no">返回上一步</router-link></el-button>
            <div slot="tip" class="el-upload__tip">只能上传一个bmp文件，且不超过500kb</div>
          </el-upload>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.centered {
  text-align: center;
}

.no {
  text-decoration: none;
  color: white;
}
</style>