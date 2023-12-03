<template>
<el-container>
<!-- <el-header>Header</el-header> -->
<el-main>
<div margin: auto>
<el-upload
class="upload-demo"
ref="upload"
action="http://127.0.0.1:5000/work"
multiple
:on-success="handleAvatarSuccess"
:on-preview="handlePreview"
:on-remove="handleRemove"
:file-list="fileList"
:auto-upload="false">
<el-button slot="trigger" size="small" type="primary">选取文件</el-button>
<el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传变化后图片</el-button>
<el-button style="margin-left: 10px;" size="small" type="primary" ><router-link to="/result" class="no">查看结果</router-link></el-button>
<el-button style="margin-left: 10px;" size="small" type="primary" ><router-link to="/vue" class="no">返回上一步</router-link></el-button>
<div slot="tip" class="el-upload__tip">只能上传一个bmp文件，且不超过500kb</div>
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

<style >
.no {
text-decoration: none;
color: white;
}
</style>