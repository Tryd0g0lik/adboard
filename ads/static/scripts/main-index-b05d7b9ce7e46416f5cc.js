/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkads"] = self["webpackChunkads"] || []).push([["index"],{

/***/ "./src/ads/app.ts":
/*!************************!*\
  !*** ./src/ads/app.ts ***!
  \************************/
/***/ (() => {

eval("/**\r\n * src\\scripts\\index.ts\r\n */\n// import { formPage } from \"./scripts/handlers/HandlerFormAd\";\n// import asyncPublicAllAd from \"src/ads/scripts/services/taskPublicAllAd\";\n// import { asyncGetListenerEvent, asyncHandlerOneAdPublic } from \"src/scripts/handleRequsetReceiveAd\";\n// import asyncTaskPublicOneAd from \"./scripts/services/taskPublicOnAd\";\n// import { handlerUserForm } from \"./scripts/handlers/handlerFormUsers/handlerRegisterForm\";\n// import { hendlerActionOfInput, subHandlerLines } from \"./scripts/handlers/handlerWeatherform/hanlerSearchPlace\";\n\nconst handlerCommmon = () => {\n  // if (window.location.pathname.includes(\"register\")) {\n\n  // Promise.all([\n  //   asyncGetListenerEvent(\"keydown\", handlerUserForm, undefined, \"form-login\")\n  // ])\n  //   .then((resolve) => {\n  //     console.log(resolve);\n  //   })\n  //   .catch((err) => {\n  //     console.log(err);\n  //   });\n  // } else if (window.location.pathname.includes(\"login\")) {\n  //   asyncGetListenerEvent(\"keydown\", handlerUserForm, undefined, \"form-login\");\n  // } else if (window.location.pathname.includes(\"weather\")) {\n\n  //   asyncGetListenerEvent(\"input\", hendlerActionOfInput, undefined, \"search\");\n  //   asyncGetListenerEvent(\"click\", subHandlerLines, undefined, \"search\");\n  // } else {\n  // formPage();\n  // publicAllAd - public all ads in HTML\n  // const idName = 'ads-collections';\n  // Promise.all([asyncPublicAllAd(), asyncGetListenerEvent(\"click\", asyncHandlerOneAdPublic, undefined, idName), asyncTaskPublicOneAd()]);\n  // }\n};\ndocument.removeEventListener(\"DOMContentLoaded\", handlerCommmon);\ndocument.addEventListener(\"DOMContentLoaded\", handlerCommmon);\n\n//# sourceURL=webpack://ads/./src/ads/app.ts?");

/***/ }),

/***/ "./src/ads/index.ts":
/*!**************************!*\
  !*** ./src/ads/index.ts ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var src_ads_app__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/ads/app */ \"./src/ads/app.ts\");\n/* harmony import */ var src_ads_app__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(src_ads_app__WEBPACK_IMPORTED_MODULE_0__);\n\n\n//# sourceURL=webpack://ads/./src/ads/index.ts?");

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ __webpack_require__.O(0, ["shared"], () => (__webpack_exec__("./src/ads/index.ts")));
/******/ var __webpack_exports__ = __webpack_require__.O();
/******/ }
]);