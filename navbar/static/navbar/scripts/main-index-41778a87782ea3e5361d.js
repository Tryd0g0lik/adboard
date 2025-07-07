"use strict";
/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(self["webpackChunkads"] = self["webpackChunkads"] || []).push([["index"],{

/***/ "./dotenv__.ts":
/*!*********************!*\
  !*** ./dotenv__.ts ***!
  \*********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   URL_HOST_FOR_API: () => (/* binding */ URL_HOST_FOR_API)\n/* harmony export */ });\nconst URL_HOST_FOR_API = \"http://83.166.245.209\";\n\n//# sourceURL=webpack://ads/./dotenv__.ts?");

/***/ }),

/***/ "./src/navbar/app.ts":
/*!***************************!*\
  !*** ./src/navbar/app.ts ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerPressButtons: () => (/* binding */ handlerPressButtons)\n/* harmony export */ });\n/* harmony import */ var src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/scripts/handleRequsetReceiveAd */ \"./src/scripts/handleRequsetReceiveAd.ts\");\n/* harmony import */ var _scripts_handlers_topMenu__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./scripts/handlers/topMenu */ \"./src/navbar/scripts/handlers/topMenu.ts\");\n/**\r\n* src\\navbar\\app.ts\r\n*/\n\n\nfunction handlerPressButtons() {\n  (0,src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_0__.asyncGetListenerEvent)('mousedown', _scripts_handlers_topMenu__WEBPACK_IMPORTED_MODULE_1__.handlerPushMenu_768, 'navbar-nav', undefined);\n  return;\n}\ndocument.removeEventListener(\"DOMContentLoaded\", handlerPressButtons);\ndocument.addEventListener(\"DOMContentLoaded\", () => {\n  console.log(\"START APP NAVBAR\");\n  handlerPressButtons();\n});\n\n//# sourceURL=webpack://ads/./src/navbar/app.ts?");

/***/ }),

/***/ "./src/navbar/scripts/handlers/topMenu.ts":
/*!************************************************!*\
  !*** ./src/navbar/scripts/handlers/topMenu.ts ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerPushMenu_768: () => (/* binding */ handlerPushMenu_768)\n/* harmony export */ });\n/**\r\n * This function runing when:\r\n * - resized of browser to the size 768 and less\r\n *  - and was cliked on the button from the '.navbar nav.navbar-nav buttom'.\r\n * When the function is run it we change the DOM:\r\n *  - In the '.navbar nav.navbar-nav > div.container-fluid' we add the 'active' class. It is\\\r\n *  we received the '.navbar nav.navbar-nav > div.container-fluid.active' and menu opened or closed.  \r\n *  \r\n * @param event \r\n * @returns \r\n */\nasync function handlerPushMenu_768(event) {\n  var _currentTarget$queryS;\n  if (window.innerWidth > 768) {\n    return;\n  }\n  const target = event.target;\n  if (!event.target || !target.classList.contains(\"navbar-toggler\") || target.type.toLowerCase() !== \"button\") {\n    return;\n  }\n  event.preventDefault();\n  event.stopPropagation();\n  const currentTarget = event.currentTarget;\n  (_currentTarget$queryS = currentTarget.querySelector(\".navbar-nav  > div:first-child\")) === null || _currentTarget$queryS === void 0 || _currentTarget$queryS.classList.toggle(\"active\");\n  return;\n}\n\n//# sourceURL=webpack://ads/./src/navbar/scripts/handlers/topMenu.ts?");

/***/ }),

/***/ "./src/scripts/handleRequsetReceiveAd.ts":
/*!***********************************************!*\
  !*** ./src/scripts/handleRequsetReceiveAd.ts ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncGetListenerEvent: () => (/* binding */ asyncGetListenerEvent),\n/* harmony export */   asyncHandlerOneAdPublic: () => (/* binding */ asyncHandlerOneAdPublic)\n/* harmony export */ });\n/* harmony import */ var _ENV__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @ENV */ \"./dotenv__.ts\");\n/**\r\n * src\\scripts\\handlers\\handlerSingleAd\\handleRequsetReceiveAd.ts\r\n */\n\nfunction handlerSubmitGetIdFroHTML(event) {\n  var _target$parentElement;\n  if (!(event.target instanceof HTMLElement)) {\n    return;\n  }\n  if (event.target.tagName.toLowerCase() !== \"button\") {\n    return;\n  }\n  event.stopPropagation();\n  event.preventDefault();\n  const target = event.target;\n  const liParantHtml = (_target$parentElement = target.parentElement) === null || _target$parentElement === void 0 || (_target$parentElement = _target$parentElement.parentElement) === null || _target$parentElement === void 0 ? void 0 : _target$parentElement.parentElement;\n  if ((liParantHtml === null || liParantHtml === void 0 ? void 0 : liParantHtml.tagName).toLowerCase() !== \"li\") {\n    console.error(\"The tag 'LI' is invalid!\");\n    return;\n  }\n  const getId = liParantHtml.hasAttribute('data-ad') ? liParantHtml.getAttribute('data-ad') : undefined;\n  if (!getId) {\n    console.error(\"The 'no id' is invalid!\");\n    return;\n  }\n  console.warn(\"THe ID of Ad is Ok.\");\n  return getId;\n}\n\n/**\r\n * This function is called when you click on the button 'submit' and get the index of the Ad.\\\r\n * Then, relocation to the page of the public Ad (http://< HOST >/ad/id/) .\r\n * @param event of click.\r\n * @returns  Promise<void>\r\n */\nasync function asyncHandlerOneAdPublic(event) {\n  // GET INDEX OF Ad FROM HTML-ELEMENT\n  const data = handlerSubmitGetIdFroHTML(event);\n  if (!data) {\n    console.warn(\"The index's data of Ad is invalid!\");\n    return;\n  }\n  window.location.href = \"\".concat(_ENV__WEBPACK_IMPORTED_MODULE_0__.URL_HOST_FOR_API, \"/user/ads/ad/\").concat(data, \"/\");\n}\n\n/**\r\n * Here, to the entrypoint accepting the 'instance' and 'className' or 'idName' (only one) of HTML-element. \\\r\n * It (html-element wich has the'className' or 'idName')\\\r\n * will receive 'instance' (a callback function), this function will be handle the events. \r\n * @param instanse: async callback c this a function that handle event 'click' by submit\r\n * @param className: string. Default value undefined. \r\n * @param idName : string. Default value undefined.\r\n * @returns void.\r\n */\nasync function asyncGetListenerEvent(eventNMame, instanse) {\n  let className = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : undefined;\n  let idName = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : undefined;\n  if (!className && idName) {\n    var _document$getElementB, _document$getElementB2;\n    (_document$getElementB = document.getElementById(idName)) === null || _document$getElementB === void 0 || _document$getElementB.removeEventListener(eventNMame, instanse);\n    (_document$getElementB2 = document.getElementById(idName)) === null || _document$getElementB2 === void 0 || _document$getElementB2.addEventListener(eventNMame, instanse);\n    return;\n  } else if (className && !idName) {\n    document.getElementsByClassName(className)[0].removeEventListener(eventNMame, instanse);\n    document.getElementsByClassName(className)[0].addEventListener(eventNMame, instanse);\n    return;\n  }\n  return;\n}\n\n//# sourceURL=webpack://ads/./src/scripts/handleRequsetReceiveAd.ts?");

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ __webpack_require__.O(0, ["shared"], () => (__webpack_exec__("./src/navbar/app.ts")));
/******/ var __webpack_exports__ = __webpack_require__.O();
/******/ }
]);