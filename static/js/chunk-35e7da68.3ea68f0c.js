(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-35e7da68"],{"120f":function(t,e,a){"use strict";var n=a("2bc8"),l=a.n(n);l.a},"2bc8":function(t,e,a){},"2bfd":function(t,e,a){"use strict";a.d(e,"b",(function(){return l})),a.d(e,"a",(function(){return r}));var n=a("b775");function l(){return Object(n["a"])({url:"/students/",method:"get"})}function r(t){return Object(n["a"])({url:"/students/"+t+"/",method:"delete"})}},"345f":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"dashboard-container"},[a("el-card",{staticClass:"box-card",attrs:{shadow:"always"}},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("div",{staticClass:"dashboard-text",staticStyle:{"text-align":"center"}},[t._v("成员管理")])]),t._v(" "),a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.students,stripe:"",border:""}},[a("el-table-column",{attrs:{prop:"student_id",label:"学号","min-width":"120",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"real_name",label:"姓名","min-width":"80",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"grade",label:"年级","min-width":"80",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"college",label:"学院","min-width":"120",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"major",label:"专业","min-width":"300",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"student_class",label:"班级","min-width":"120",sortable:"",align:"center"}}),t._v(" "),a("el-table-column",{attrs:{prop:"update_time",label:"更新时间","min-width":"120",sortable:"",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[t._v("\n          "+t._s(e.row["update_time"].substr(0,10))+"\n        ")]}}])}),t._v(" "),a("el-table-column",{attrs:{prop:"",label:"操作",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-button",{attrs:{size:"small",type:"danger"},on:{click:function(a){return t.handleDelete(e.row.id)}}},[t._v("删除")])]}}])})],1)],1)],1)},l=[],r=a("db72"),s=a("2f62"),c=a("2bfd"),i={name:"Membership",data:function(){return{students:null}},computed:Object(r["a"])({},Object(s["b"])(["name"])),created:function(){this.fetchData()},methods:{fetchData:function(){var t=this;Object(c["b"])().then((function(e){t.students=e}))},handleDelete:function(t){var e=this;Object(c["a"])(t).then((function(){e.fetchData()}))}}},o=i,u=(a("120f"),a("2877")),d=Object(u["a"])(o,n,l,!1,null,"50d2b18c",null);e["default"]=d.exports}}]);