<template>
  <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="项目介绍" name="first" style="width:75%; margin:auto;">
      <p class="text">
          SAR 图像变化检测是对同一地区不同时相的两幅或多幅图像进行分析，检测出其中的变化部分与未变化部分，检测局部纹理和辐射值的变化是图像变化检测的主要任务。图像的变化是由图像场景的真实变化，或由传感器精度、照射角、地面湿度等变化而引起的。在实际应用中，SAR图像变化检测技术在各方面都发挥重要作用。如在民用领域，主要是对资源和环境监测中各种变化信息的获取，例如对农业中的作物生长进行监测；土地覆盖率变化、水域变化、森林和植被变化、城市变迁、地形改变等；测绘中的地理空间数据更新；以及自然灾害中对火灾、泥石流、水灾等造成的损失的评测。
      </p>
      <p class="text">
          大规模的土地管理、监测需要一个智能、高效的统计和检测方法， 但是光学遥感技术受制于视角、天气、光照和分辨率等因素，成像效果远不能满足数据精准度和完整度的需求。
      </p>
      <p class="text">
          我们的项目《星影变动：SAR图像变化检测》是为了解决大规模上土地管理、规划和决策工作者获得各项数据不够直观、大量数据难以处理的难点而产生的图像处理软件。
          ,通过SAR图像变化检测的方法，基于神经网络的图像处理技术使其能为用户带来资源与环境监测方面的便利：如及时更新大范围地表环境地理空间数据，监测土地利用率以及土地覆盖状况、森林以及植被的覆盖率、城市的扩张状况、道路路况变化等，为各行业提供科学依据和参考。
      </p>
      <p class="text">
          项目仓库:<a href="//github.com/OUC-2023autumn-Group5/StardowChange" target="blank" style="color:rgb(38,201,255)">https://github.com/OUC-2023autumn-Group5/StardowChange</a>
      </p>
    </el-tab-pane>
    <el-tab-pane label="小组介绍" name="second" style="width:75%; margin:auto;">
      <div style="display: flex; flex-wrap: wrap; justify-content: center; font-size: 12px;">
      <div class="personal_data">
        <div class="container">
          <img class="profile_picture" src="touxian1.jpg" width="250px" height="250px">
        </div>
        <div class="text_padding">
          <p class="text">
            姓名:王星苹
          </p>
          <p class="text">
            职位:组长
          </p>
          <p class="text">
            负责工作:后端开发
          </p >
          <p class="text">
            QQ邮箱:2924368393@qq.com
          </p>
        </div>
      </div>
      <div class="personal_data">
        <div class="container">
          <img class="profile_picture" src="touxian3.jpg" width="250px" height="250px">
        </div>
        <div class="text_padding">
          <p class="text">
            姓名:王祥
          </p>
          <p class="text">
            职位:组员
          </p>
          <p class="text">
            负责工作:后端开发
          </p >
          <p class="text">
            QQ邮箱:2842771441@qq.com
          </p>
        </div>
      </div>
      <div class="personal_data">
        <div class="container">
          <img class="profile_picture" src="touxian2.jpg" width="250px" height="250px">
        </div>
        <div class="text_padding">
          <p class="text">
            姓名:董继坤
          </p>
          <p class="text">
            职位:组员
          </p>
          <p class="text">
            负责工作:前端开发
          </p >
          <p class="text">
            QQ邮箱:3052737956@qq.com
          </p>
        </div>
      </div>
      <div class="personal_data">
        <div class="container">
          <img class="profile_picture" src="logo.jpg" width="250px" height="250px">
        </div>
        <div class="text_padding">
          <p class="text">
            姓名:李满鹏
          </p>
          <p class="text">
            职位:组员
          </p>
          <p class="text">
            负责工作:前端开发
          </p >
          <p class="text">
            QQ邮箱:3177663988@qq.com
          </p>
        </div>
      </div>
    </div>
    </el-tab-pane>
    <el-tab-pane label="参考样例" name="third" style="width:75%; margin:auto;">
      <p>以下展示的是使用我们模型进行sar图像变化检测的例子(前两张图为要检测的图,最后一张为输出的结果)</p>
      <div>
        <img src="before.bmp" width="250px" height="250px" style="vertical-align:middle;margin:50px 50px"> 
        <img src="after.bmp" width="250px" height="250px" style="vertical-align:middle;margin:50px 50px">
        <img src="Figure_1.png" width="350px" height="350px" style="vertical-align:middle;margin:50px 50px">
      </div>
      <div>
        <img src="ottawa_1.bmp" width="250px" height="250px" style="vertical-align:middle;margin:50px 50px"> 
        <img src="ottawa_2.bmp" width="250px" height="250px" style="vertical-align:middle;margin:50px 50px">
        <img src="Figure_2.png" width="350px" height="350px" style="vertical-align:middle;margin:50px 50px">
      </div>
    </el-tab-pane>
    <el-tab-pane label="开始检测" name="fourth" style="width:75%; margin:auto;">
      <div class='butt'>
        <el-button type="primary" ><router-link to="/vue" class='input'>开始使用</router-link></el-button>
      </div>
    </el-tab-pane>
  </el-tabs>
</template>
<script>
   export default {
    data() {
      return {
        activeName: 'first'
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      }
    }
  };
</script>

<style >
.input{
    text-decoration: none;
    color: white;
}
p {
  display: block;
  margin-top: 1em;
  margin-bottom: 1em;
  margin-left: 0;
  margin-right: 0;
}
.text{
  font-size: 120%;
}
.butt {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* 可根据实际需要调整高度 */
}
body{
  background-color: rgb(39,39,39); 
  color:white
}
.profile_picture{
    border-radius: 100%;
    border: 5px solid white;
    transition: all;
    transition-duration: 1s;
    transition-timing-function: ease-in-out;
    display: block;
    margin: auto;
    width: 60%;
    height: 60%;
    display: block;
    position: absolute; /* Take your picture out of the flow */
    top: 0;
    bottom: 0;
    left: 50%;
    right: 50%; /* Make the picture taking the size of it's parent */
    width: 100%; /* This if for the object-fit */
    height: 100%; /* This if for the object-fit */
    object-fit: cover; /* Equivalent of the background-size: cover; of a background-image */
    object-position: center;
}
.profile_picture:hover{
    border: 5px solid #BBB;
    transform: scale(1.05);
}
.text_padding{
    padding: 0 10% 0 10%;
}
.el-tabs__nav-scroll{
    background-color: rgb(39,39,39);
}
.el-tabs__item{
  color:white;
}
.personal_data{
    width: 35%; 
    min-width: 100px;
    max-width: 600px;
    border: 4px dotted rgb(38,201,255) ;
    border-radius: 20px; 
    background-color: rgb(22,34,38); 
    padding: 20px;
    margin: 5px;
}
.container {
  position: relative;
  width: 50%; 
}
.container:after {
  content: "";
  display: block;
  padding-bottom: 100%; 
}
.el-tabs--bottom .el-tabs__item.is-bottom:nth-child(2), .el-tabs--bottom .el-tabs__item.is-top:nth-child(2), .el-tabs--top .el-tabs__item.is-bottom:nth-child(2), .el-tabs--top .el-tabs__item.is-top:nth-child(2) {
    padding-left: 20px;
}
.el-tabs--bottom .el-tabs__item.is-bottom:last-child, .el-tabs--bottom .el-tabs__item.is-top:last-child, .el-tabs--top .el-tabs__item.is-bottom:last-child, .el-tabs--top .el-tabs__item.is-top:last-child {
    padding-right: 20px;
}
.el-tabs__item.is-active {
    color: rgb(38,201,255);
    background: rgb(22,34,38);
    border-radius: 5px 5px 0 0;
    border: 2px solid rgb(38,201,255);
}
.el-tabs__nav-wrap::after {
    background-color: rgb(38,201,255);
}
.el-tabs__active-bar.is-top{
    background-color: rgba(0,0,0,0);
}
</style>