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

/***/ "./src/adboard/app.ts":
/*!****************************!*\
  !*** ./src/adboard/app.ts ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/scripts/handleRequsetReceiveAd */ \"./src/scripts/handleRequsetReceiveAd.ts\");\n/* harmony import */ var _scripts_handlers_handlerFormUsers_handlerRegisterForm__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./scripts/handlers/handlerFormUsers/handlerRegisterForm */ \"./src/adboard/scripts/handlers/handlerFormUsers/handlerRegisterForm.ts\");\n/**\r\n* src\\scripts\\index.ts\r\n*/\n\n\nconst handlerCommmon = () => {\n  if (window.location.pathname.includes(\"login\")) {\n    (0,src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_0__.asyncGetListenerEvent)(\"keydown\", _scripts_handlers_handlerFormUsers_handlerRegisterForm__WEBPACK_IMPORTED_MODULE_1__.handlerUserForm, undefined, \"form-login\");\n  }\n};\ndocument.removeEventListener(\"DOMContentLoaded\", handlerCommmon);\ndocument.addEventListener(\"DOMContentLoaded\", handlerCommmon);\n\n//# sourceURL=webpack://ads/./src/adboard/app.ts?");

/***/ }),

/***/ "./src/adboard/index.ts":
/*!******************************!*\
  !*** ./src/adboard/index.ts ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var src_adboard_app__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/adboard/app */ \"./src/adboard/app.ts\");\n\n\n//# sourceURL=webpack://ads/./src/adboard/index.ts?");

/***/ }),

/***/ "./src/adboard/scripts/handlers/handlerFormUsers/handlerRegisterForm.ts":
/*!******************************************************************************!*\
  !*** ./src/adboard/scripts/handlers/handlerFormUsers/handlerRegisterForm.ts ***!
  \******************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerUserForm: () => (/* binding */ handlerUserForm)\n/* harmony export */ });\n/* harmony import */ var src_adboard_scripts_services_cookies_setCookies__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/adboard/scripts/services/cookies/setCookies */ \"./src/adboard/scripts/services/cookies/setCookies.ts\");\n/* harmony import */ var src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! src/adboard/scripts/services/taskGetErrorContent */ \"./src/adboard/scripts/services/taskGetErrorContent.ts\");\n/* harmony import */ var src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/scripts/validators/validateLength */ \"./src/scripts/validators/validateLength.ts\");\n/* harmony import */ var src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/scripts/validators/validateRegex */ \"./src/scripts/validators/validateRegex.ts\");\n/**\r\n * src\\scripts\\handlers\\handlerFormUsers\\handlerRegisterForm.ts\r\n */\n\n\n\n\n\n/**\r\n * src\\scripts\\handlers\\handlerFormUsers\\handlerRegisterForm.ts\r\n */\nconst URL_HOST_FOR_API = process.env.URL_HOST_FOR_API || \"localhost\";\n\n/***\r\n * Function that handle user's forms. It is the registration form and login form.\r\n * @param: event: KeyboardEvent ('to the 'Enter'keydown')\r\n */\nasync function handlerUserForm(event) {\n  var _querySelector;\n  if (!event.key || event.key && event.key.toLowerCase() !== \"enter\") {\n    return;\n  }\n  ;\n  const pathname = location.pathname;\n  // GET DATA FROM FORM\n  const body_ = {};\n  // body_.method = \"GET\";\n  const currentTarget = event.currentTarget;\n  const formHtml = currentTarget.querySelector(\"form\");\n  const form = new FormData(formHtml);\n\n  // PREVENT DEFAULT\n  event.preventDefault();\n  event.stopPropagation();\n\n  // SEND DATA TO API\n  body_.method = \"POST\";\n  body_.body = form;\n  // CHECK VALIDITY USERNAME\n  const title = form.get('username');\n  const regexUsername = /(^[a-zA-Z][a-zA-Z_]{2,30}$|^$)/;\n  const regexEmail = /(^[a-zA-Z0-9]{3,50}@{1}[a-zA-Z]{2,30}\\.[a-zA-Z]{2,5}$|^$)/;\n  (_querySelector = currentTarget.querySelector(\".invalid\")) === null || _querySelector === void 0 || _querySelector.remove();\n  try {\n    // VALIDATE TITLE AD\n    await Promise.all([(0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMinLength)(title, 3), (0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMaxLength)(title, 30), (0,src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_3__.validateRegex)(title, regexUsername)]);\n  } catch (err) {\n    const fieldHTML = currentTarget.querySelector('input[name=\"username\"]');\n    (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(fieldHTML, err);\n    return;\n  }\n  if (form.get('email') || (typeof form.get('email')).includes(\"string\") && form.get('email').length == 0) {\n    try {\n      // VALIDATE EMAIL\n      const email = form.get('email');\n      await Promise.all([(0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMinLength)(email, 3), (0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMaxLength)(email, 50), (0,src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_3__.validateRegex)(email, regexEmail)]);\n    } catch (err) {\n      const fieldHTML = currentTarget.querySelector('input[name=\"email\"]');\n      (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(fieldHTML, err);\n      return;\n    }\n  }\n  ;\n\n  // CHECK VALIDITY PASSWORD\n  const password = form.get('password');\n  const regexPassword = /(^[a-zA-Z%0-9}{_%]{2,30}$|^$)/;\n  try {\n    // VALIDATE TITLE AD\n    await Promise.all([(0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMinLength)(title, 3), (0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMaxLength)(title, 30), (0,src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_3__.validateRegex)(password, regexPassword)]);\n  } catch (err) {\n    const fieldHTML = currentTarget.querySelector('input[name=\"password\"]');\n    (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(fieldHTML, err);\n    return;\n  }\n  if (form.get('confirm_password') || (typeof form.get('confirm_password')).includes(\"string\") && form.get('confirm_password').length == 0) {\n    // CHECK VALIDITY CONFIRM PASSWORD\n    const confirmPassword = form.get('confirm_password');\n    if (confirmPassword !== password) {\n      const fieldHTML = currentTarget.querySelector('input[name=\"confirm_password\"]');\n      const err = new Error(\"err: Check the passwords.\");\n      (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(fieldHTML, err);\n      return;\n    }\n  }\n\n  // LOGIN OR REGISTER USER\n  // const pathnemr = (pathname.includes(\"login\")) ? '/api/v2/users/login_user/' : \"/api/v2/users/\";\n  // REGISTER USER\n  const templeteApi = pathname.includes(\"login\") ? \"/api/v1/users/index/0/login_user/\" : '/api/v1/users/index/';\n  // REGISTER USER\n  const url = new URL(templeteApi, URL_HOST_FOR_API);\n  try {\n    const response = await fetch(url, body_);\n    if (!response.ok || response.status > 201) {\n      console.warn(\"User form invalid: \".concat(response.statusText));\n      return;\n    }\n    const data = await response.json();\n    // CHANGE LOCATION\n    if (pathname.includes(\"register\")) {\n      setTimeout(() => window.location.pathname = \"/login/\", 200);\n    } else {\n      Array.from(data[\"data\"]).forEach(elementtoken => {\n        // console.log(`data ${elementtoken}: `, data[elementtoken]);\n        if (Object.keys(elementtoken).includes(\"token_access\")) {\n          const k = \"token_access\";\n          const v = Object(elementtoken)[k];\n          const liveTime = Object(elementtoken)[k];\n          (0,src_adboard_scripts_services_cookies_setCookies__WEBPACK_IMPORTED_MODULE_0__.setSessionIdInCookie)(k, v, liveTime);\n        } else {\n          const k = \"token_refresh\";\n          const v = Object(elementtoken)[k];\n          const liveTime = Object(elementtoken)[k];\n          (0,src_adboard_scripts_services_cookies_setCookies__WEBPACK_IMPORTED_MODULE_0__.setSessionIdInCookie)(k, v, liveTime);\n          window.location.pathname = \"/weather/\";\n        }\n      });\n    }\n  } catch (error) {\n    console.error(\"USER FORM ERROR: \", error.message);\n    throw new Error(\"USER FORM ERROR: \".concat(error));\n  }\n}\n;\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/handlers/handlerFormUsers/handlerRegisterForm.ts?");

/***/ }),

/***/ "./src/adboard/scripts/services/cookies/setCookies.ts":
/*!************************************************************!*\
  !*** ./src/adboard/scripts/services/cookies/setCookies.ts ***!
  \************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   setSessionIdInCookie: () => (/* binding */ setSessionIdInCookie)\n/* harmony export */ });\n/***\r\n * src\\scripts\\services\\cookies\\setCoocie.ts\r\n */\n\n/**\r\n * Cookies set up\r\n * @param key \r\n * @param value \r\n * @param lifeTime \r\n */\nfunction setSessionIdInCookie(key, value, lifeTime) {\n  const cookieName = key;\n  const cookieValue = value;\n  // const maxAge = 60 * 60 * 24; // Время жизни cookie в секундах (например, 1 день)\n\n  document.cookie = \"\".concat(cookieName, \"=\").concat(cookieValue, \"; max-age=\").concat(lifeTime, \"; path=/; secure; samesite=strict\");\n}\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/services/cookies/setCookies.ts?");

/***/ }),

/***/ "./src/adboard/scripts/services/taskGetErrorContent.ts":
/*!*************************************************************!*\
  !*** ./src/adboard/scripts/services/taskGetErrorContent.ts ***!
  \*************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/**\r\n * src\\scripts\\services\\taskGetErrorContent.ts\r\n */\n\n/**\r\n * For a chacker of validate from from conten.    \r\n * @param field HTML element.\r\n * @param err \r\n * @returns void\r\n */\nconst getErrorContent = (field, err) => {\n  const pHtml = document.createElement('p');\n  pHtml.className = \"invalid\";\n  const fieldHtml = field;\n  const textInput = fieldHtml.value ? fieldHtml.value : \"\";\n  pHtml.textContent = \"\".concat(err.message.split(\": \")[1]);\n  field.after(pHtml);\n  field.value = textInput;\n  return false;\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (getErrorContent);\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/services/taskGetErrorContent.ts?");

/***/ }),

/***/ "./src/scripts/handleRequsetReceiveAd.ts":
/*!***********************************************!*\
  !*** ./src/scripts/handleRequsetReceiveAd.ts ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncGetListenerEvent: () => (/* binding */ asyncGetListenerEvent),\n/* harmony export */   asyncHandlerOneAdPublic: () => (/* binding */ asyncHandlerOneAdPublic)\n/* harmony export */ });\n/**\r\n * src\\scripts\\handlers\\handlerSingleAd\\handleRequsetReceiveAd.ts\r\n */\n\nconst URL_HOST_FOR_API = process.env.URL_HOST_FOR_API || \"localhost\";\nfunction handlerSubmitGetIdFroHTML(event) {\n  var _target$parentElement;\n  if (!(event.target instanceof HTMLElement)) {\n    return;\n  }\n  if (event.target.tagName.toLowerCase() !== \"button\") {\n    return;\n  }\n  event.stopPropagation();\n  event.preventDefault();\n  const target = event.target;\n  const liParantHtml = (_target$parentElement = target.parentElement) === null || _target$parentElement === void 0 || (_target$parentElement = _target$parentElement.parentElement) === null || _target$parentElement === void 0 ? void 0 : _target$parentElement.parentElement;\n  if ((liParantHtml === null || liParantHtml === void 0 ? void 0 : liParantHtml.tagName).toLowerCase() !== \"li\") {\n    console.error(\"The tag 'LI' is invalid!\");\n    return;\n  }\n  const getId = liParantHtml.hasAttribute('data-ad') ? liParantHtml.getAttribute('data-ad') : undefined;\n  if (!getId) {\n    console.error(\"The 'no id' is invalid!\");\n    return;\n  }\n  console.warn(\"THe ID of Ad is Ok.\");\n  return getId;\n}\n\n/**\r\n * This function is called when you click on the button 'submit' and get the index of the Ad.\\\r\n * Then, relocation to the page of the public Ad (http://< HOST >/ad/id/) .\r\n * @param event of click.\r\n * @returns  Promise<void>\r\n */\nasync function asyncHandlerOneAdPublic(event) {\n  // GET INDEX OF Ad FROM HTML-ELEMENT\n  const data = handlerSubmitGetIdFroHTML(event);\n  if (!data) {\n    console.warn(\"The index's data of Ad is invalid!\");\n    return;\n  }\n  window.location.href = \"\".concat(URL_HOST_FOR_API, \"/ad/\").concat(data, \"/\");\n}\n\n/**\r\n * Here, to the entrypoint accepting the 'instance' and 'className' or 'idName' (only one) of HTML-element. \\\r\n * It (html-element wich has the'className' or 'idName')\\\r\n * will receive 'instance' (a callback function), this function will be handle the events. \r\n * @param instanse: async callback c this a function that handle event 'click' by submit\r\n * @param className: string. Default value undefined. \r\n * @param idName : string. Default value undefined.\r\n * @returns void.\r\n */\nasync function asyncGetListenerEvent(eventNMame, instanse) {\n  let className = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : undefined;\n  let idName = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : undefined;\n  if (!className && idName) {\n    var _document$getElementB, _document$getElementB2;\n    (_document$getElementB = document.getElementById(idName)) === null || _document$getElementB === void 0 || _document$getElementB.removeEventListener(eventNMame, instanse);\n    (_document$getElementB2 = document.getElementById(idName)) === null || _document$getElementB2 === void 0 || _document$getElementB2.addEventListener(eventNMame, instanse);\n    return;\n  } else if (className && !idName) {\n    document.getElementsByClassName(className)[0].removeEventListener(eventNMame, instanse);\n    document.getElementsByClassName(className)[0].addEventListener(eventNMame, instanse);\n    return;\n  }\n  return;\n}\n\n//# sourceURL=webpack://ads/./src/scripts/handleRequsetReceiveAd.ts?");

/***/ }),

/***/ "./src/scripts/validators/validateLength.ts":
/*!**************************************************!*\
  !*** ./src/scripts/validators/validateLength.ts ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   validateMaxLength: () => (/* binding */ validateMaxLength),\n/* harmony export */   validateMinLength: () => (/* binding */ validateMinLength)\n/* harmony export */ });\n/**\r\n * src\\scripts\\validators\\validateLength.ts\r\n */\n\n/**\r\n * \r\n * @param value : strin - The string to validate\r\n * @param maxLength : number - The maximum length of the string\r\n */\nasync function validateMinLength(value, minLength) {\n  if (!value || value.length < minLength) {\n    throw new Error('validateMinLength: Invalid value');\n  }\n}\n\n/**\r\n * \r\n * @param value : strin - The string to validate\r\n * @param maxLength : number - The maximum length of the string\r\n */\nasync function validateMaxLength(value, maxLength) {\n  if (!value || value.length > maxLength) {\n    throw new Error('validateMinLength: Invalid value');\n  }\n}\n\n//# sourceURL=webpack://ads/./src/scripts/validators/validateLength.ts?");

/***/ }),

/***/ "./src/scripts/validators/validateRegex.ts":
/*!*************************************************!*\
  !*** ./src/scripts/validators/validateRegex.ts ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   validateRegex: () => (/* binding */ validateRegex)\n/* harmony export */ });\n/**\r\n * src\\scripts\\validators\\validateRegex.ts\r\n */\nasync function validateRegex(value, regex) {\n  const bool = regex.test(value);\n  if (!bool) {\n    throw new Error(' validateRegex: Value is not valid');\n  }\n}\n\n//# sourceURL=webpack://ads/./src/scripts/validators/validateRegex.ts?");

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ __webpack_require__.O(0, ["shared"], () => (__webpack_exec__("./src/adboard/index.ts")));
/******/ var __webpack_exports__ = __webpack_require__.O();
/******/ }
]);