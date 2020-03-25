(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-404242aa"],{"2f5a":function(t,e,a){},cae1:function(t,e,a){"use strict";a.r(e);var l=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"dashboard-container"},[a("el-card",{staticClass:"box-card",attrs:{shadow:"always"}},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("div",{staticClass:"dashboard-text",staticStyle:{"text-align":"center"}},[t._v("活动管理")])]),t._v(" "),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.actsLoading,expression:"actsLoading"}],staticStyle:{width:"100%"},attrs:{data:t.acts,"element-loading-text":"Loading",stripe:"",border:""}},[a("el-table-column",{attrs:{prop:"real_name",label:"负责人","min-width":"100",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"title",label:"活动名称","min-width":"200",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"week",label:"周数","min-width":"200",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"day",label:"星期","min-width":"80",sortable:"",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(t.dayString[e.row.day]))])]}}])}),t._v(" "),a("el-table-column",{attrs:{prop:"time",label:"时间","min-width":"120",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"",label:"操作",align:"center","min-width":"160"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-button",{attrs:{size:"mini",type:"primary"},on:{click:function(a){return t.handleActDialog(e.row)}}},[t._v("编辑")]),t._v(" "),a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){return t.handleActDelete(e.row.id)}}},[t._v("删除")])]}}])})],1),t._v(" "),a("el-col",{attrs:{span:24}},[a("el-button",{staticClass:"el-table-add-row",attrs:{type:"info",plain:"",disabled:"admin"!==t.role},on:{click:function(e){return t.handleActDialog(t.actNull)}}},[t._v(" + 添加 ")])],1)],1),t._v(" "),a("el-dialog",{attrs:{title:"活动详情",visible:t.dialogFormVisible,width:"75%"},on:{"update:visible":function(e){t.dialogFormVisible=e}}},[a("el-form",{ref:"ACT",attrs:{model:t.act,"label-width":"auto","label-position":"left",rules:t.rules}},[a("el-form-item",{attrs:{label:"活动名称",prop:"title"}},[a("el-input",{attrs:{autocomplete:"off"},model:{value:t.act.title,callback:function(e){t.$set(t.act,"title",e)},expression:"act.title"}})],1),t._v(" "),a("el-form-item",{attrs:{label:"活动周数",prop:"week"}},[a("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择活动周数",filterable:""},model:{value:t.act.week,callback:function(e){t.$set(t.act,"week",e)},expression:"act.week"}},t._l(20,(function(t){return a("el-option",{key:t,attrs:{label:t,value:t}})})),1)],1),t._v(" "),a("el-form-item",{attrs:{label:"活动星期",prop:"day"}},[a("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择活动星期",filterable:""},model:{value:t.act.day,callback:function(e){t.$set(t.act,"day",e)},expression:"act.day"}},t._l(t.dayString,(function(t,e){return a("el-option",{key:e,attrs:{label:t,value:e}})})),1)],1),t._v(" "),a("el-form-item",{attrs:{label:"活动时间",prop:"time"}},[a("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择活动时间",filterable:""},model:{value:t.act.time,callback:function(e){t.$set(t.act,"time",e)},expression:"act.time"}},t._l(10,(function(t){return a("el-option",{key:t,attrs:{label:"第"+t+"节课",value:t}})})),1)],1),t._v(" "),a("el-form-item",{attrs:{label:"活动负责人",prop:"leader"}},[a("el-select",{staticStyle:{width:"100%"},attrs:{placeholder:"请选择活动负责人",filterable:""},model:{value:t.act.leader,callback:function(e){t.$set(t.act,"leader",e)},expression:"act.leader"}},t._l(t.students,(function(t,e){return a("el-option",{key:e,attrs:{label:t[0]+" "+t[1],value:e}})})),1)],1)],1),t._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:t.cancelActDialog}},[t._v("取 消")]),t._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:t.confirmActDialog}},[t._v("保 存")])],1)],1)],1)},n=[],i=(a("6b54"),a("ac6a"),a("db72")),r=a("2f62"),c=a("b775");function o(t){return Object(c["a"])({url:"/acts/",method:"post",data:t})}function s(){return Object(c["a"])({url:"/acts/",method:"get"})}function d(t,e){return Object(c["a"])({url:"/acts/"+t+"/",method:"put",data:e})}function u(t){return Object(c["a"])({url:"/acts/"+t+"/",method:"delete"})}var f=a("2bfd"),b={name:"Act",data:function(){return{students:{},acts:null,act:{id:null,title:null,week:null,day:null,time:null,leader:null,real_name:null},actNull:{id:null,title:null,week:null,day:null,time:null,leader:null,real_name:null},actsLoading:!0,dialogFormVisible:!1,dayString:{1:"星期一",2:"星期二",3:"星期三",4:"星期四",5:"星期五",6:"星期六",7:"星期日"},rules:{title:[{required:!0,message:"请输入活动名称",trigger:"blur"}],week:[{required:!0,message:"请选择活动周数",trigger:"blur"}],day:[{required:!0,message:"请选择活动星期",trigger:"blur"}],time:[{required:!0,message:"请选择活动时间",trigger:"blur"}],leader:[{required:!0,message:"请选择活动负责人",trigger:"blur"}]}}},computed:Object(i["a"])({},Object(r["b"])(["name","role"])),created:function(){this.fetchStudentAct()},methods:{fetchStudentAct:function(){var t=this;Object(f["c"])().then((function(e){e.forEach((function(e){t.students[e.id]=[e.student_id,e.real_name]})),t.fetchAct()}))},fetchAct:function(){var t=this;this.actsLoading=!0,s().then((function(e){e.forEach((function(e){e["real_name"]=t.students[e.leader][1],e["leader"]=e["leader"].toString()})),t.acts=e,t.actsLoading=!1})).catch((function(){t.acts=null,t.actsLoading=!1}))},handleActDialog:function(t){this.act=JSON.parse(JSON.stringify(t)),this.dialogFormVisible=!0,this.$refs["ACT"].resetFields()},cancelActDialog:function(){this.dialogFormVisible=!1},confirmActDialog:function(){var t=this;this.$refs["ACT"].validate((function(e){if(!e)return console.log("error submit!!"),!1;null===t.act.id?t.handleActCreate(t.act):t.handleActEdit(t.act),t.dialogFormVisible=!1}))},handleActCreate:function(t){var e=this;o(t).then((function(){e.fetchAct()}))},handleActEdit:function(t){var e=this;d(t.id,t).then((function(){e.fetchAct()}))},handleActDelete:function(t){var e=this;u(t).then((function(){e.fetchAct()}))}}},m=b,h=(a("d569"),a("2877")),p=Object(h["a"])(m,l,n,!1,null,"3c280c18",null);e["default"]=p.exports},d569:function(t,e,a){"use strict";var l=a("2f5a"),n=a.n(l);n.a}}]);