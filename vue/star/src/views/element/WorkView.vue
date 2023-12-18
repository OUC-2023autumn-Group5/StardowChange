<template>
  <el-container class="upload-container">
    <el-main>
      <div  class="container2">模型运行需要时间，需要大概五到七分钟</div>
      <div class="container1">
        <el-upload
          class="avatar-uploader"
          action="http://127.0.0.1:5000/upload1"
          :show-file-list="false"
          :on-success="handleAvatarSuccess1"
          :before-upload="beforeAvatarUpload"
        >
          <img v-if="imageUrl1" :src="imageUrl1" class="avatar" />
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
        
        <el-upload
          class="avatar-uploader"
          action="http://127.0.0.1:5000/upload2"
          :show-file-list="false"
          :on-success="handleAvatarSuccess2"
          :before-upload="beforeAvatarUpload"
        >
          <img v-if="imageUrl2" :src="imageUrl2" class="avatar" />
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
        
      </div>
    
      <div class='container1'>
        <img id ="png-img" src="" alt="PNG Image" style="display:none" >

      </div>
      <div class='container1'>
        <el-button type="primary" ><router-link to="/" class="no">返回首页</router-link></el-button>
        <el-button type="primary" @click="startWork">开始工作</el-button>
      </div>
    </el-main>

  </el-container>
</template>

<script>
// import axios from 'axios';
export default {
    data() {
      return {
        imageUrl1: '',
        imageUrl2: ''
      };
    },
    methods: {
      handleAvatarSuccess1(res, file) {
        this.imageUrl1 = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        //this.imageUrl1 = URL.createObjectURL(file.raw);
        const isBMP = file.type === 'image/bmp';
        const isLt2M = file.size / 1024 / 1024 < 2;
        if (!isBMP) {
          this.$message.error('上传头像图片只能是 bmp 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传图片大小不能超过 2MB!');
        }
        return isBMP && isLt2M;
      },
      handleAvatarSuccess2(res, file) {
        this.imageUrl2 = URL.createObjectURL(file.raw);
      },
      startWork() {
          fetch('http://127.0.0.1:5000/work', {
            timeout:300000,
    method: 'GET',
  })
  .then((response) => {
    // 请求成功后，获取返回的 BMP 图片 URL
    return response.url;
  })
  .then((url) => {
    // 将 BMP 图片显示在页面上
    document.getElementById("png-img").src = url;
    document.getElementById("png-img").style.display = "block";
  })
  .catch((error) => {
    // 请求失败，输出错误信息
    console.error('Error:', error);
  });
}
    }
  }
</script>

<style>
body{
  background-color: rgb(39,39,39); 
  color:white
}
.no {
  text-decoration: none;
  color: white;
}

.el-button {
  margin-right: 10px;
}
.container1 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 32vh;

}
.container2{
  display: flex;
  justify-content: center;
  align-items: center；
}
.centered {
  text-align: center;
}
.upload-container {
  background-color: #f2f2f2;
  padding: 20px;
  border: 1px solid #ccc;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: rgb(39,39,39); 
}
.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>