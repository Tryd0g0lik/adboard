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

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   URL_HOST_FOR_API: () => (/* binding */ URL_HOST_FOR_API)\n/* harmony export */ });\nconst URL_HOST_FOR_API = \"http://127.0.0.1:8000\";\n\n//# sourceURL=webpack://ads/./dotenv__.ts?");

/***/ }),

/***/ "./src/adboard/app.ts":
/*!****************************!*\
  !*** ./src/adboard/app.ts ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _ADBoards_handlers_loginLogout__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @ADBoards-handlers/loginLogout */ \"./src/adboard/scripts/handlers/loginLogout.ts\");\n/**\r\n* src\\adboard\\scripts\\services\\taskGetErrorContent.ts\r\n*/\n\ndocument.removeEventListener(\"DOMContentLoaded\", () => _ADBoards_handlers_loginLogout__WEBPACK_IMPORTED_MODULE_0__.handlerLoginLogout);\ndocument.addEventListener(\"DOMContentLoaded\", () => {\n  console.log(\"START APP\");\n  (0,_ADBoards_handlers_loginLogout__WEBPACK_IMPORTED_MODULE_0__.handlerLoginLogout)();\n});\n\n//# sourceURL=webpack://ads/./src/adboard/app.ts?");

/***/ }),

/***/ "./src/adboard/scripts/handlers/handlerFormUsers/handlerRegisterForm.ts":
/*!******************************************************************************!*\
  !*** ./src/adboard/scripts/handlers/handlerFormUsers/handlerRegisterForm.ts ***!
  \******************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerUserForm: () => (/* binding */ handlerUserForm)\n/* harmony export */ });\n/* harmony import */ var src_adboard_scripts_services_cookies_setCookies__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/adboard/scripts/services/cookies/setCookies */ \"./src/adboard/scripts/services/cookies/setCookies.ts\");\n/* harmony import */ var src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! src/adboard/scripts/services/taskGetErrorContent */ \"./src/adboard/scripts/services/taskGetErrorContent.ts\");\n/* harmony import */ var src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/scripts/validators/validateLength */ \"./src/scripts/validators/validateLength.ts\");\n/* harmony import */ var src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/scripts/validators/validateRegex */ \"./src/scripts/validators/validateRegex.ts\");\n/* harmony import */ var _ENV__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @ENV */ \"./dotenv__.ts\");\n/**\r\n * src\\adboard\\scripts\\handlers\\handlerFormUsers\\handlerRegisterForm.ts\r\n */\n\n\n\n\n\n\n// import { URL_HOST_FOR_API } from \"@ENV\";\n\n/***\r\n * Function that handle user's forms. It is the registration form and login form.\r\n * @param: event: KeyboardEvent ('to the 'Enter'keydown')\r\n */\nasync function handlerUserForm(event) {\n  var _querySelector;\n  console.log('REGISTER FORM');\n  if (!event.key || event.key && event.key.toLowerCase() !== \"enter\") {\n    return;\n  }\n  ;\n  const pathname = location.pathname;\n  // GET DATA FROM FORM\n  const body_ = {};\n  // body_.method = \"GET\";\n  const currentTarget = event.currentTarget;\n  const formHtml = currentTarget.querySelector(\"form\");\n  const form = new FormData(formHtml);\n\n  // PREVENT DEFAULT\n  event.preventDefault();\n  event.stopPropagation();\n\n  // SEND DATA TO API\n  body_.method = \"POST\";\n  body_.body = form;\n  // CHECK VALIDITY USERNAME\n  const title = form.get('username').trim();\n  const regexUsername = /(^[a-zA-Z][a-zA-Z_0-9]{2,29}$|^$)/;\n  const regexEmail = /(^[a-zA-Z0-9]{3,50}@{1}[a-zA-Z]{2,30}\\.[a-zA-Z]{2,5}$|^$)/;\n  (_querySelector = currentTarget.querySelector(\".invalid\")) === null || _querySelector === void 0 || _querySelector.remove();\n  try {\n    // VALIDATE TITLE AD\n    await Promise.all([(0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMinLength)(title, 3), (0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMaxLength)(title, 30), (0,src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_3__.validateRegex)(title, regexUsername)]);\n  } catch (err) {\n    const fieldHTML = currentTarget.querySelector('input[name=\"username\"]');\n    (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(fieldHTML, err);\n    return;\n  }\n  const email = form.get('email');\n  if (email && email.includes(\"@\") || (typeof form.get('email')).includes(\"string\") && form.get('email').length == 0) {\n    try {\n      // VALIDATE EMAIL\n      const email = form.get('email').trim();\n      await Promise.all([(0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMinLength)(email, 3), (0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMaxLength)(email, 50), (0,src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_3__.validateRegex)(email, regexEmail)]);\n    } catch (err) {\n      const fieldHTML = currentTarget.querySelector('input[name=\"email\"]');\n      (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(fieldHTML, err);\n      return;\n    }\n  }\n  ;\n\n  // CHECK VALIDITY PASSWORD\n  const password = form.get('password');\n  const regexPassword = /(^[a-zA-Z%0-9{_%]{2,29}$|^$)/;\n  const confirmPassword = form.get('confirm_password');\n  try {\n    // VALIDATE TITLE AD\n    await Promise.all([(0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMinLength)(title, 3), (0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_2__.validateMaxLength)(title, 30), (0,src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_3__.validateRegex)(password, regexPassword)]);\n  } catch (err) {\n    const fieldHTML = currentTarget.querySelector('input[name=\"password\"]');\n    (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(fieldHTML, err);\n    return;\n  }\n  if (confirmPassword || (typeof form.get('confirm_password')).includes(\"string\") && form.get('confirm_password').length == 0) {\n    // CHECK VALIDITY CONFIRM PASSWORD ;\n    if (confirmPassword.trim() !== password.trim()) {\n      const fieldHTML = currentTarget.querySelector('input[name=\"confirm_password\"]');\n      const err = new Error(\"err: Check the passwords.\");\n      (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(fieldHTML, err);\n      return;\n    }\n  }\n\n  // LOGIN OR REGISTER USER\n  // const pathnemr = (pathname.includes(\"login\")) ? '/api/v2/users/login_user/' : \"/api/v2/users/\";\n  // REGISTER USER\n  const templeteApi = pathname.includes(\"login\") ? \"/api/v1/users/index/0/login_user/\" : '/api/v1/users/index/';\n  // REGISTER USER\n  const url = new URL(templeteApi, _ENV__WEBPACK_IMPORTED_MODULE_4__.URL_HOST_FOR_API);\n  try {\n    const response = await fetch(url, body_);\n    if (!response.ok || response.status > 201) {\n      console.warn(\"User form invalid: \".concat(response.statusText));\n      return;\n    }\n    const data = await response.json();\n    // CHANGE LOCATION\n    if (pathname.includes(\"register\")) {\n      setTimeout(() => window.location.pathname = \"/users/login/\", 200);\n    } else {\n      Array.from(data[\"data\"]).forEach(elementtoken => {\n        // console.log(`data ${elementtoken}: `, data[elementtoken]);\n        if (Object.keys(elementtoken).includes(\"token_access\")) {\n          const k = \"token_access\";\n          const v = Object(elementtoken)[k];\n          const keyLifeTime = Object.keys(elementtoken)[1];\n          const liveTime = Math.round(parseFloat(Object(elementtoken)[keyLifeTime]));\n          (0,src_adboard_scripts_services_cookies_setCookies__WEBPACK_IMPORTED_MODULE_0__.setSessionIdInCookie)(k, v, String(liveTime));\n        } else {\n          const k = \"token_refresh\";\n          const v = Object(elementtoken)[k];\n          const keyLifeTime = Object.keys(elementtoken)[1];\n          const liveTime = Math.round(Object(elementtoken)[keyLifeTime]);\n          (0,src_adboard_scripts_services_cookies_setCookies__WEBPACK_IMPORTED_MODULE_0__.setSessionIdInCookie)(k, v, String(liveTime));\n          window.location.pathname = \"/\";\n        }\n      });\n    }\n  } catch (error) {\n    console.error(\"USER FORM ERROR: \", error.message);\n    throw new Error(\"USER FORM ERROR: \".concat(error));\n  }\n}\n;\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/handlers/handlerFormUsers/handlerRegisterForm.ts?");

/***/ }),

/***/ "./src/adboard/scripts/handlers/handlerLogout/handlerReRequestLogout.ts":
/*!******************************************************************************!*\
  !*** ./src/adboard/scripts/handlers/handlerLogout/handlerReRequestLogout.ts ***!
  \******************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerRequestLogout: () => (/* binding */ handlerRequestLogout)\n/* harmony export */ });\n/* harmony import */ var _ENV__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @ENV */ \"./dotenv__.ts\");\n/**\r\n * src/adboard/scripts/handlers/handlerLogout/handlerReRequestLogout.ts\r\n */\n\nasync function handlerRequestLogout() {\n  await fetch(_ENV__WEBPACK_IMPORTED_MODULE_0__.URL_HOST_FOR_API + \"/api/v1/users/index/0/logout_user\", {\n    \"method\": \"GET\"\n  });\n  window.location.href = \"/users/login/\";\n}\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/handlers/handlerLogout/handlerReRequestLogout.ts?");

/***/ }),

/***/ "./src/adboard/scripts/handlers/handlerLogout/handlerbuttonLogout.ts":
/*!***************************************************************************!*\
  !*** ./src/adboard/scripts/handlers/handlerLogout/handlerbuttonLogout.ts ***!
  \***************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerButtonUserLogout: () => (/* binding */ handlerButtonUserLogout)\n/* harmony export */ });\n/**\r\n * src\\adboard\\scripts\\handlers\\handlerLogout\\handlerbuttonLogout.ts\r\n */\n\n/**\r\n * \r\n * @param e keydown event\r\n * @returns \r\n */\nfunction handlerButtonUserLogout(e) {\n  if (e.target.tagName.toLowerCase() !== 'a' || e.target.textContent.toLowerCase() !== 'logout') {\n    return false;\n  }\n  return true;\n}\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/handlers/handlerLogout/handlerbuttonLogout.ts?");

/***/ }),

/***/ "./src/adboard/scripts/handlers/loginLogout.ts":
/*!*****************************************************!*\
  !*** ./src/adboard/scripts/handlers/loginLogout.ts ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   handlerLoginLogout: () => (/* binding */ handlerLoginLogout)\n/* harmony export */ });\n/* harmony import */ var src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/scripts/handleRequsetReceiveAd */ \"./src/scripts/handleRequsetReceiveAd.ts\");\n/* harmony import */ var _ADBoards_handlers_handlerFormUsers_handlerRegisterForm__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @ADBoards-handlers/handlerFormUsers/handlerRegisterForm */ \"./src/adboard/scripts/handlers/handlerFormUsers/handlerRegisterForm.ts\");\n/* harmony import */ var _ADBoards_scripts_services_taskLogoutUser__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @ADBoards/scripts/services/taskLogoutUser */ \"./src/adboard/scripts/services/taskLogoutUser.ts\");\n/**\r\n * src\\adboard\\scripts\\handlers\\loginLogout.ts\r\n */\n\n\n\nfunction handlerLoginLogout() {\n  if (window.location.pathname.includes(\"login\") ||\n  // LOGIN INTERFECE ADDING TO THE NAVBAR.\n  window.location.pathname.includes('register')) {\n    console.log(\"START REGISTER\");\n    (0,src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_0__.asyncGetListenerEvent)(\"keydown\", _ADBoards_handlers_handlerFormUsers_handlerRegisterForm__WEBPACK_IMPORTED_MODULE_1__.handlerUserForm, undefined, \"form-login\");\n  }\n  ;\n  // LOGOUT INTERFECE ADDEING TO THE NAVBAR.\n  (0,src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_0__.asyncGetListenerEvent)(\"click\", _ADBoards_scripts_services_taskLogoutUser__WEBPACK_IMPORTED_MODULE_2__.taskLogoutUser, undefined, \"logout\");\n}\n;\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/handlers/loginLogout.ts?");

/***/ }),

/***/ "./src/adboard/scripts/services/cookies/setCookies.ts":
/*!************************************************************!*\
  !*** ./src/adboard/scripts/services/cookies/setCookies.ts ***!
  \************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   setSessionIdInCookie: () => (/* binding */ setSessionIdInCookie)\n/* harmony export */ });\n/***\r\n * src\\adboard\\scripts\\services\\cookies\\setCookies.ts\r\n */\n\n/**\r\n * Cookies set up\r\n * @param key \r\n * @param value \r\n * @param lifeTime \r\n */\nfunction setSessionIdInCookie(key, value, lifeTime) {\n  const cookieName = key;\n  const cookieValue = value;\n  // const maxAge = 60 * 60 * 24; // Время жизни cookie в секундах (например, 1 день)\n\n  document.cookie = \"\".concat(cookieName, \"=\").concat(cookieValue, \"; max-age=\").concat(lifeTime, \"; path=/; samesite=strict\");\n}\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/services/cookies/setCookies.ts?");

/***/ }),

/***/ "./src/adboard/scripts/services/taskGetErrorContent.ts":
/*!*************************************************************!*\
  !*** ./src/adboard/scripts/services/taskGetErrorContent.ts ***!
  \*************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/**\r\n * src\\adboard\\scripts\\services\\taskGetErrorContent.ts\r\n */\n\n/**\r\n * For a chacker of validate from from conten.    \r\n * @param field HTML element.\r\n * @param err \r\n * @returns void\r\n */\nconst getErrorContent = (field, err) => {\n  const pHtml = document.createElement('p');\n  pHtml.className = \"invalid\";\n  const fieldHtml = field;\n  const textInput = fieldHtml.value ? fieldHtml.value : \"\";\n  pHtml.textContent = \"\".concat(err.message.split(\": \")[1]);\n  field.after(pHtml);\n  field.value = textInput;\n  return false;\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (getErrorContent);\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/services/taskGetErrorContent.ts?");

/***/ }),

/***/ "./src/adboard/scripts/services/taskLogoutUser.ts":
/*!********************************************************!*\
  !*** ./src/adboard/scripts/services/taskLogoutUser.ts ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   taskLogoutUser: () => (/* binding */ taskLogoutUser)\n/* harmony export */ });\n/* harmony import */ var _ADBoards_handlers_handlerLogout_handlerReRequestLogout__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @ADBoards-handlers/handlerLogout/handlerReRequestLogout */ \"./src/adboard/scripts/handlers/handlerLogout/handlerReRequestLogout.ts\");\n/* harmony import */ var _ADBoards_handlers_handlerLogout_handlerbuttonLogout__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @ADBoards-handlers/handlerLogout/handlerbuttonLogout */ \"./src/adboard/scripts/handlers/handlerLogout/handlerbuttonLogout.ts\");\n/***\r\n * src\\adboard\\scripts\\services\\taskLogoutUser.ts\r\n */\n\n\n\nconst taskLogoutUser = async event => {\n  const resultBoolean = (0,_ADBoards_handlers_handlerLogout_handlerbuttonLogout__WEBPACK_IMPORTED_MODULE_1__.handlerButtonUserLogout)(event);\n  if (!resultBoolean) {\n    return;\n  }\n  await (0,_ADBoards_handlers_handlerLogout_handlerReRequestLogout__WEBPACK_IMPORTED_MODULE_0__.handlerRequestLogout)();\n};\n\n//# sourceURL=webpack://ads/./src/adboard/scripts/services/taskLogoutUser.ts?");

/***/ }),

/***/ "./src/ads/app.ts":
/*!************************!*\
  !*** ./src/ads/app.ts ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _ADBS_handlers_HandlerFormAd__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @ADBS-handlers/HandlerFormAd */ \"./src/ads/scripts/handlers/HandlerFormAd/index.ts\");\n/* harmony import */ var _ADS_scripts_services_taskPublicAllAd__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @ADS/scripts/services/taskPublicAllAd */ \"./src/ads/scripts/services/taskPublicAllAd.ts\");\n/* harmony import */ var src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/scripts/handleRequsetReceiveAd */ \"./src/scripts/handleRequsetReceiveAd.ts\");\n/* harmony import */ var _ADS_scripts_services_taskPublicOnAd__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @ADS/scripts/services/taskPublicOnAd */ \"./src/ads/scripts/services/taskPublicOnAd.ts\");\n/* harmony import */ var _ADS_scripts_services_taskChangeId__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @ADS/scripts/services/taskChangeId */ \"./src/ads/scripts/services/taskChangeId.ts\");\n/**\r\n * src\\scripts\\index.ts\r\n */\n\n\n\n\n\nconst handlerCommmon = () => {\n  const formPagePromise = new Promise(resolve => {\n    (0,_ADBS_handlers_HandlerFormAd__WEBPACK_IMPORTED_MODULE_0__.formPage)();\n    resolve(true);\n  });\n\n  // publicAllAd - public all ads in HTML\n  const idName = 'ads-collections';\n  Promise.allSettled([(0,_ADS_scripts_services_taskChangeId__WEBPACK_IMPORTED_MODULE_4__.taskChangeIdDOM)(), formPagePromise, (0,_ADS_scripts_services_taskPublicAllAd__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(), (0,src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_2__.asyncGetListenerEvent)(\"click\", src_scripts_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_2__.asyncHandlerOneAdPublic, undefined, idName), (0,_ADS_scripts_services_taskPublicOnAd__WEBPACK_IMPORTED_MODULE_3__[\"default\"])()]);\n};\ndocument.removeEventListener(\"DOMContentLoaded\", handlerCommmon);\ndocument.addEventListener(\"DOMContentLoaded\", handlerCommmon);\n\n//# sourceURL=webpack://ads/./src/ads/app.ts?");

/***/ }),

/***/ "./src/ads/index.ts":
/*!**************************!*\
  !*** ./src/ads/index.ts ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var src_adboard_app__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/adboard/app */ \"./src/adboard/app.ts\");\n/* harmony import */ var src_ads_app__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! src/ads/app */ \"./src/ads/app.ts\");\n\n\n\n//# sourceURL=webpack://ads/./src/ads/index.ts?");

/***/ }),

/***/ "./src/ads/scripts/handlers/HandlerFormAd/hendlerRequst.ts":
/*!*****************************************************************!*\
  !*** ./src/ads/scripts/handlers/HandlerFormAd/hendlerRequst.ts ***!
  \*****************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerRequestAddAd: () => (/* binding */ asyncHandlerRequestAddAd)\n/* harmony export */ });\n/* harmony import */ var _ENV__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @ENV */ \"./dotenv__.ts\");\n/**\r\n * src\\sripts\\handlers\\HandlerFormAd\\hendlerRequst.ts\r\n */\n\n\n/**\r\n * This make the post-request to server, it adds the one a new Ad.\r\n * @param event Mouse click.\r\n * @returns boolean or AdLine\r\n */\nconst asyncHandlerRequestAddAd = async event => {\n  event.stopPropagation();\n  // GET FORM HTML FOR AD\n  const currenttarget = event.currentTarget;\n  // GET DATA OF FORM\n  const dataF0rm = new FormData(currenttarget);\n  try {\n    // REQUEST TO SERVER AND SEND AD's DATA OF FORM\n    console.log(\" REQUEST TO SERVER AND SEND AD's DATA OF FORM;\");\n    const response = await fetch(\"\".concat(_ENV__WEBPACK_IMPORTED_MODULE_0__.URL_HOST_FOR_API, \"/api/v1/ads/index/\"), {\n      method: \"POST\",\n      body: dataF0rm\n    });\n    if (!response.ok) {\n      const body = await response.json();\n      console.log(\"RESPONSE OF AD NOT Ok\", body[\"detail\"][0]);\n      return false;\n    }\n    // CLEANING THE BODY OF FORM HTML\n    currenttarget.querySelectorAll(\"input\").forEach(input => {\n      input.value = \"\";\n    });\n    currenttarget.querySelectorAll(\"textarea\").forEach(textarea => {\n      textarea.value = \"\";\n    });\n    //  GET JSON DATA\n    const body = await response.json();\n    // RESPONCE OF AD IS OK\n    console.log(\"RESPONCE OF AD IS OK: \".concat(body));\n    const data = JSON.parse(body);\n    return data;\n  } catch (error) {\n    console.log(\"AD REQUEST ERROR => \".concat(error));\n    return false;\n  }\n};\n\n//# sourceURL=webpack://ads/./src/ads/scripts/handlers/HandlerFormAd/hendlerRequst.ts?");

/***/ }),

/***/ "./src/ads/scripts/handlers/HandlerFormAd/index.ts":
/*!*********************************************************!*\
  !*** ./src/ads/scripts/handlers/HandlerFormAd/index.ts ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   formPage: () => (/* binding */ formPage)\n/* harmony export */ });\n/* harmony import */ var src_ads_scripts_handlers_HandlerFormImg__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/ads/scripts/handlers/HandlerFormImg */ \"./src/ads/scripts/handlers/HandlerFormImg/index.ts\");\n/* harmony import */ var _handlersAdsCollection_handlerReceiveNewAd__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../handlersAdsCollection/handlerReceiveNewAd */ \"./src/ads/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts\");\n/* harmony import */ var _hendlerRequst__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./hendlerRequst */ \"./src/ads/scripts/handlers/HandlerFormAd/hendlerRequst.ts\");\n/* harmony import */ var src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! src/scripts/validators/validateLength */ \"./src/scripts/validators/validateLength.ts\");\n/* harmony import */ var src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! src/scripts/validators/validateRegex */ \"./src/scripts/validators/validateRegex.ts\");\n/* harmony import */ var src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! src/adboard/scripts/services/taskGetErrorContent */ \"./src/adboard/scripts/services/taskGetErrorContent.ts\");\n/**\r\n * src\\sripts\\handlers\\HandlerFormAd\\index.ts\r\n */\n\n\n\n\n\n\nconst asyncGetDataForm = async e => {\n  var _querySelector;\n  // GET SUBMIT HTML\n  if (e.target && e.target.tagName.toLowerCase() !== \"button\") {\n    return false;\n  }\n  console.log(\"START FORM's HANDLER OF AD\");\n  e.preventDefault();\n  // GET FORM HTML FOR AD\n  const currenttarget = e.currentTarget;\n  if (currenttarget && currenttarget.tagName.toLowerCase() !== \"form\") {\n    return false;\n  }\n  (_querySelector = currenttarget.querySelector(\".invalid\")) === null || _querySelector === void 0 || _querySelector.remove();\n  // GET DATA OF FORM\n  const dataF0rm = new FormData(currenttarget);\n  // CHECK TITLE OF AD FORM\n  const title = dataF0rm.get('title').trim();\n  const regexTitle = /^[a-zA-Zа-яА-ЯёЁ][\\w ,\\-_\\dа-яёА-ЯЁ0-9]{1,98}[a-zA-Zа-яА-ЯёЁ0-9!\\.\\?]$/;\n  // const regexTitle = /^(?!.*  )[a-zA-Zа-яА-ЯёЁ][\\w ,\\-_\\dа-яёА-ЯЁ0-9]{1,98}[a-zA-Zа-яА-ЯёЁ0-9]$[^\\S\\W \\\\]?/;\n\n  try {\n    // VALIDATE TITLE AD\n    await Promise.all([(0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_3__.validateMinLength)(title, 3), (0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_3__.validateMaxLength)(title, 100), (0,src_scripts_validators_validateRegex__WEBPACK_IMPORTED_MODULE_4__.validateRegex)(title, regexTitle)]);\n  } catch (err) {\n    const titleHTML = currenttarget.querySelector('input[name=\"title\"]');\n    (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_5__[\"default\"])(titleHTML, err);\n    return false;\n  }\n  // CHECK DESCRIPTION AD FORM\n  try {\n    const description = dataF0rm.get('description').trim();\n    await Promise.all([(0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_3__.validateMinLength)(description, 10), (0,src_scripts_validators_validateLength__WEBPACK_IMPORTED_MODULE_3__.validateMaxLength)(description, 500)]);\n  } catch (err) {\n    const titleHTML = currenttarget.querySelector('textarea[name=\"description\"]');\n    (0,src_adboard_scripts_services_taskGetErrorContent__WEBPACK_IMPORTED_MODULE_5__[\"default\"])(titleHTML, err);\n    return false;\n  }\n  const dataBoolJson = await (0,_hendlerRequst__WEBPACK_IMPORTED_MODULE_2__.asyncHandlerRequestAddAd)(e);\n  if ((typeof dataBoolJson).toLowerCase() === 'boolean') {\n    return false;\n  }\n  const dataJson = dataBoolJson;\n  // ONE AD  SEND TO PUBLIC IN WEB-PAGE\n  (0,_handlersAdsCollection_handlerReceiveNewAd__WEBPACK_IMPORTED_MODULE_1__.asyncHandlerReceivesData)(dataJson.data);\n  return true;\n};\nconst getImg = async e => {\n  const responce = await (0,src_ads_scripts_handlers_HandlerFormImg__WEBPACK_IMPORTED_MODULE_0__.asyncHandlerRequestAddImage)(e);\n  if (!responce) {\n    console.log(\"RESPONSE OF SEND IMAGE IS NOT OK\");\n    return false;\n  }\n  return true;\n};\n\n/**\r\n * This function for add the two listens to the form, the first is for send ads to server, and the second is for send image file to server.\r\n * @returns boolean.\r\n */\nfunction formPage() {\n  // ADS FORM\n  const formHTML = document.querySelector(\".form form\");\n  // IMAGE FILE FORM\n  const formImageFileHTML = document.querySelector(\".form form.ads-form__full-image-file\");\n  if (!formHTML) {\n    console.log(\"Somewing that frong! Invalid form.\");\n    return false;\n  } else {\n    const formHTMLCopy = formHTML;\n    // ----- EVENT ONCLICK FOR ADS -----\n    formHTMLCopy.onclick = asyncGetDataForm;\n  }\n  if (!formImageFileHTML) {\n    console.log(\"Somewing that frong! Invalid form.\");\n    return false;\n  } else {\n    const formHTMLCopy = formImageFileHTML;\n    //----- EVENT ONCLICK FOR IMAGE -----\n    formHTMLCopy.onclick = getImg;\n  }\n  return true;\n}\n\n//# sourceURL=webpack://ads/./src/ads/scripts/handlers/HandlerFormAd/index.ts?");

/***/ }),

/***/ "./src/ads/scripts/handlers/HandlerFormImg/index.ts":
/*!**********************************************************!*\
  !*** ./src/ads/scripts/handlers/HandlerFormImg/index.ts ***!
  \**********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerRequestAddImage: () => (/* binding */ asyncHandlerRequestAddImage)\n/* harmony export */ });\n/* harmony import */ var _ENV__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @ENV */ \"./dotenv__.ts\");\n/**\r\n * src\\sripts\\handlers\\HandlerFormImg\\index.ts\r\n */\n\n/**\r\n * This handler of post request for add only one an image to server.\r\n * @param event handler of clik by button of form. This form load the image to server.\r\n * @returns  AdLine or boolean\r\n */\nconst asyncHandlerRequestAddImage = async event => {\n  event.stopPropagation();\n\n  // GET SUBMIT HTML\n  if (event.target && event.target.tagName.toLowerCase() !== \"button\") {\n    return false;\n  }\n  event.preventDefault();\n  // GET FORM HTML\n  const currenttarget = event.currentTarget;\n  if (currenttarget && currenttarget.tagName.toLowerCase() !== \"form\") {\n    return false;\n  }\n  const dataF0rm = new FormData(currenttarget);\n  // REQUEST TO SERVER AND SEND FILE IMAGE\n  try {\n    const response = await fetch(\"\".concat(_ENV__WEBPACK_IMPORTED_MODULE_0__.URL_HOST_FOR_API, \"/api/v1/image/\"), {\n      method: \"POST\",\n      body: dataF0rm\n    });\n    if (!response.ok) {\n      return false;\n    }\n    // RESPONCE IS OK\n    const body = await response.json();\n    console.log(\"SERVER: \".concat(body));\n    return body;\n  } catch (error) {\n    console.log(\"Request of FIleImage to server Error => \".concat(error));\n    return false;\n  }\n};\n\n//# sourceURL=webpack://ads/./src/ads/scripts/handlers/HandlerFormImg/index.ts?");

/***/ }),

/***/ "./src/ads/scripts/handlers/handlerSingleAd/handlerGetOneAd.ts":
/*!*********************************************************************!*\
  !*** ./src/ads/scripts/handlers/handlerSingleAd/handlerGetOneAd.ts ***!
  \*********************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerRequestGetOneAd: () => (/* binding */ asyncHandlerRequestGetOneAd)\n/* harmony export */ });\n/**\r\n * src\\scripts\\handlers\\handlerSingleAd\\handlerGetOneAd.ts\r\n */\n\n/**\r\n * @param: pathname string. This is the path of api.  Exemple - '/api/ad/one/'.\r\n * @param index type stryng. This is the indes of the ad. It is an one data line from server.\r\n * @returns json data (`{ data: AdLine[] `)\r\n */\nasync function asyncHandlerRequestGetOneAd(pathname, index) {\n  try {\n    const response = await fetch(\"\".concat(pathname).concat(index), {\n      method: 'GET',\n      headers: {\n        'Content-Type': 'application/json'\n      }\n    });\n    if (!response.ok) {\n      console.error(\"The 'error' of GET: \".concat(response.statusText));\n      return;\n    }\n    const data = await response.json();\n    const dataJson = JSON.parse(data);\n    return dataJson;\n  } catch (err) {\n    console.error(new Error(\"The 'index' ERROR: \" + err));\n  }\n  return;\n}\n\n//# sourceURL=webpack://ads/./src/ads/scripts/handlers/handlerSingleAd/handlerGetOneAd.ts?");

/***/ }),

/***/ "./src/ads/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts":
/*!*******************************************************************************!*\
  !*** ./src/ads/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts ***!
  \*******************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerReceivesData: () => (/* binding */ asyncHandlerReceivesData)\n/* harmony export */ });\n/* harmony import */ var src_ads_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/ads/scripts/services/taskCreateOneElement */ \"./src/ads/scripts/services/taskCreateOneElement.ts\");\n/**\r\n * src\\sripts\\handlers\\handlersAdsCollection\\handlerReceiveNewAd.ts\r\n */\n\n\n/**\r\n * This handler for publicate the one new ad or list of ads's collection in web-page.\r\n * @param content Adline's or AdLinesCollection data type. Default value is undefined.\r\n * @returns Promise boolean\r\n */\nasync function asyncHandlerReceivesData() {\n  let content = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : undefined;\n  if (!content) {\n    /**\r\n     * Дополнителььная функция request для запроса get получить  список ads\r\n     */\n    null;\n    return true;\n  }\n  const collectionsHTML = document.querySelector(\"#ads-collections ul.ads-views\");\n  if (!collectionsHTML) {\n    console.log(\"INVALID 'ads-collections'\");\n    false;\n  } else {\n    // RECEIVING HTML CONTENT FROM SERVER's/API's DATA\n    if (!Array.isArray(content)) {\n      (0,src_ads_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(collectionsHTML, content);\n    } else content.forEach(item => {\n      (0,src_ads_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(collectionsHTML, item);\n    });\n  }\n  // ulHtml\n  return true;\n}\n;\n\n//# sourceURL=webpack://ads/./src/ads/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts?");

/***/ }),

/***/ "./src/ads/scripts/handlers/handlersAdsCollection/handlerRequestlCollection.ts":
/*!*************************************************************************************!*\
  !*** ./src/ads/scripts/handlers/handlersAdsCollection/handlerRequestlCollection.ts ***!
  \*************************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerGetAdsCollection: () => (/* binding */ asyncHandlerGetAdsCollection)\n/* harmony export */ });\n/* harmony import */ var _ENV__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @ENV */ \"./dotenv__.ts\");\n/**\r\n * src\\scripts\\handlers\\handlersAdsCollection\\handlerRequestlCollection.ts\r\n * */\n\n/**\r\n * This function is download the collection of the ads from server.\r\n * @returns {data: AdLinesCollection} | void\r\n */\nasync function asyncHandlerGetAdsCollection() {\n  try {\n    // REQUEST GET COLLECTION ADS\n    const url = new URL(\"\".concat(_ENV__WEBPACK_IMPORTED_MODULE_0__.URL_HOST_FOR_API, \"/api/v1/ads/index/\"));\n    const response = await fetch(url, {\n      method: \"GET\"\n    });\n    if (!response.ok) {\n      console.error(\"The Ads downloads data invalid!\");\n      return;\n    }\n    // RESEIVING RESPONSE DATA IN JSON TYPE\n    const responseData = await response.json();\n    const data = JSON.parse(responseData);\n    return data;\n  } catch (err) {\n    console.log(\"Error: \".concat(err.message));\n  }\n  return;\n}\n\n//# sourceURL=webpack://ads/./src/ads/scripts/handlers/handlersAdsCollection/handlerRequestlCollection.ts?");

/***/ }),

/***/ "./src/ads/scripts/services/taskChangeId.ts":
/*!**************************************************!*\
  !*** ./src/ads/scripts/services/taskChangeId.ts ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   taskChangeIdDOM: () => (/* binding */ taskChangeIdDOM)\n/* harmony export */ });\n/**\r\n *  src\\ads\\scripts\\services\\taskChangeId.ts\r\n */\n\n/**\r\n * Change the ID of DOM element to the ads page.\r\n * @returns void\r\n */\nconst taskChangeIdDOM = () => {\n  const sectionHtml = document.getElementById(\"form-login\");\n  if (!sectionHtml) {\n    return;\n  }\n  ;\n  sectionHtml.id = \"form-ads\";\n};\n\n//# sourceURL=webpack://ads/./src/ads/scripts/services/taskChangeId.ts?");

/***/ }),

/***/ "./src/ads/scripts/services/taskCreateOneElement.ts":
/*!**********************************************************!*\
  !*** ./src/ads/scripts/services/taskCreateOneElement.ts ***!
  \**********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/**\r\n * src\\scripts\\services\\createOneElement.ts\r\n */\n\n/**\r\n * \r\n * @param instance HTMLElement This is main BOX for inserting by one line of ads\r\n * @param content AdLine's type. It is object (or json data) from server/api\r\n * @returns void\r\n  */\nconst teskInsertOneAd = (instance, content) => {\n  // CREATE THE PARENT CONTEXT's BOX \n  const newLineHtml = document.createElement('li');\n  newLineHtml.className = 'ad-view';\n  newLineHtml.dataset.ad = \"\".concat(content.id);\n\n  // CREATE CONTENT CONTAINER\n  const viewContentHTml = document.createElement('div');\n  viewContentHTml.className = 'ad-view-container';\n  // CREATE TITLE\n  const titleAdHtml = document.createElement('div');\n  titleAdHtml.className = 'ad-view-title';\n  const titleHeading = document.createElement('h2');\n  titleHeading.textContent = content.title;\n  titleAdHtml.append(titleHeading);\n\n  // CREATE DESCRIPTION\n  const contextAdHtml = document.createElement('div');\n  contextAdHtml.className = 'ad-view-content';\n  contextAdHtml.textContent = content.description;\n\n  // CREATE FOOTER\n  const viewFooterHtml = document.createElement('div');\n  viewFooterHtml.className = 'ad-view-footer';\n  const button = document.createElement('button');\n  button.type = 'submit';\n  button.className = 'ad-moving btn btn-primary';\n  button.textContent = 'Перейти';\n  viewFooterHtml.append(button);\n\n  // ASSEMBLE ALL PARTS\n  viewContentHTml.append(titleAdHtml);\n  viewContentHTml.append(contextAdHtml);\n  viewContentHTml.append(viewFooterHtml);\n  newLineHtml.append(viewContentHTml);\n\n  // PUBLICATION TO WEB PAGE\n  instance.append(newLineHtml);\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (teskInsertOneAd);\n\n//# sourceURL=webpack://ads/./src/ads/scripts/services/taskCreateOneElement.ts?");

/***/ }),

/***/ "./src/ads/scripts/services/taskPublicAllAd.ts":
/*!*****************************************************!*\
  !*** ./src/ads/scripts/services/taskPublicAllAd.ts ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var src_ads_scripts_handlers_handlersAdsCollection_handlerRequestlCollection__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/ads/scripts/handlers/handlersAdsCollection/handlerRequestlCollection */ \"./src/ads/scripts/handlers/handlersAdsCollection/handlerRequestlCollection.ts\");\n/* harmony import */ var _handlers_handlersAdsCollection_handlerReceiveNewAd__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../handlers/handlersAdsCollection/handlerReceiveNewAd */ \"./src/ads/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts\");\n/**\r\n * src\\scripts\\services\\taskPublicAllAd.ts\r\n */\n\n\n\n/**\r\n * This function is responsible for requesting the collection of ads and publishing them in the HTML.\r\n * @returns void\r\n */\nconst asyncPublicAllAd = async () => {\n  // REQUEST GET COLLECTION ADS\n  const response = await (0,src_ads_scripts_handlers_handlersAdsCollection_handlerRequestlCollection__WEBPACK_IMPORTED_MODULE_0__.asyncHandlerGetAdsCollection)();\n  if (!response) {\n    console.error(\"Error fetching ads!\");\n    return;\n  }\n  // PUBLICT COLLECTION OF ADS ON HTML\n  await (0,_handlers_handlersAdsCollection_handlerReceiveNewAd__WEBPACK_IMPORTED_MODULE_1__.asyncHandlerReceivesData)(response[\"data\"]);\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (asyncPublicAllAd);\n\n//# sourceURL=webpack://ads/./src/ads/scripts/services/taskPublicAllAd.ts?");

/***/ }),

/***/ "./src/ads/scripts/services/taskPublicOnAd.ts":
/*!****************************************************!*\
  !*** ./src/ads/scripts/services/taskPublicOnAd.ts ***!
  \****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var src_ads_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/ads/scripts/services/taskCreateOneElement */ \"./src/ads/scripts/services/taskCreateOneElement.ts\");\n/* harmony import */ var src_ads_scripts_handlers_handlerSingleAd_handlerGetOneAd__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! src/ads/scripts/handlers/handlerSingleAd/handlerGetOneAd */ \"./src/ads/scripts/handlers/handlerSingleAd/handlerGetOneAd.ts\");\n/**\r\n * src\\scripts\\services\\taskPublicOnAd.ts\r\n */\n\n\n\nconst asyncTaskPublicOneAd = async () => {\n  // GET ID OF AD FROM THE URL\n  const pathname = window.location.pathname;\n  const index = pathname.split(\"/\")[4];\n  if (!index) {\n    return;\n  }\n  // GET DATA OF AD FROM THE SERVER\n  const response = await (0,src_ads_scripts_handlers_handlerSingleAd_handlerGetOneAd__WEBPACK_IMPORTED_MODULE_1__.asyncHandlerRequestGetOneAd)('/api/v1/ads/index/', index);\n  if (!response) {\n    console.error(\"The received data from server is invalid!\");\n    return;\n  }\n  const sectionHtml = document.getElementById(\"ad-page-container\");\n  if (!sectionHtml) {\n    console.error(\"The section HTML is invalid!\");\n    return;\n  }\n  // PUBLIC AD ON AD PAGE\n  (0,src_ads_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(sectionHtml, response.data[0]);\n  const buttonHtml = document.querySelector(\".ad-view-footer button\");\n  if (!buttonHtml) {\n    return;\n  }\n  buttonHtml.remove();\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (asyncTaskPublicOneAd);\n\n//# sourceURL=webpack://ads/./src/ads/scripts/services/taskPublicOnAd.ts?");

/***/ }),

/***/ "./src/scripts/handleRequsetReceiveAd.ts":
/*!***********************************************!*\
  !*** ./src/scripts/handleRequsetReceiveAd.ts ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncGetListenerEvent: () => (/* binding */ asyncGetListenerEvent),\n/* harmony export */   asyncHandlerOneAdPublic: () => (/* binding */ asyncHandlerOneAdPublic)\n/* harmony export */ });\n/* harmony import */ var _ENV__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @ENV */ \"./dotenv__.ts\");\n/**\r\n * src\\scripts\\handlers\\handlerSingleAd\\handleRequsetReceiveAd.ts\r\n */\n\nfunction handlerSubmitGetIdFroHTML(event) {\n  var _target$parentElement;\n  if (!(event.target instanceof HTMLElement)) {\n    return;\n  }\n  if (event.target.tagName.toLowerCase() !== \"button\") {\n    return;\n  }\n  event.stopPropagation();\n  event.preventDefault();\n  const target = event.target;\n  const liParantHtml = (_target$parentElement = target.parentElement) === null || _target$parentElement === void 0 || (_target$parentElement = _target$parentElement.parentElement) === null || _target$parentElement === void 0 ? void 0 : _target$parentElement.parentElement;\n  if ((liParantHtml === null || liParantHtml === void 0 ? void 0 : liParantHtml.tagName).toLowerCase() !== \"li\") {\n    console.error(\"The tag 'LI' is invalid!\");\n    return;\n  }\n  const getId = liParantHtml.hasAttribute('data-ad') ? liParantHtml.getAttribute('data-ad') : undefined;\n  if (!getId) {\n    console.error(\"The 'no id' is invalid!\");\n    return;\n  }\n  console.warn(\"THe ID of Ad is Ok.\");\n  return getId;\n}\n\n/**\r\n * This function is called when you click on the button 'submit' and get the index of the Ad.\\\r\n * Then, relocation to the page of the public Ad (http://< HOST >/ad/id/) .\r\n * @param event of click.\r\n * @returns  Promise<void>\r\n */\nasync function asyncHandlerOneAdPublic(event) {\n  // GET INDEX OF Ad FROM HTML-ELEMENT\n  const data = handlerSubmitGetIdFroHTML(event);\n  if (!data) {\n    console.warn(\"The index's data of Ad is invalid!\");\n    return;\n  }\n  window.location.href = \"\".concat(_ENV__WEBPACK_IMPORTED_MODULE_0__.URL_HOST_FOR_API, \"/user/ads/ad/\").concat(data, \"/\");\n}\n\n/**\r\n * Here, to the entrypoint accepting the 'instance' and 'className' or 'idName' (only one) of HTML-element. \\\r\n * It (html-element wich has the'className' or 'idName')\\\r\n * will receive 'instance' (a callback function), this function will be handle the events. \r\n * @param instanse: async callback c this a function that handle event 'click' by submit\r\n * @param className: string. Default value undefined. \r\n * @param idName : string. Default value undefined.\r\n * @returns void.\r\n */\nasync function asyncGetListenerEvent(eventNMame, instanse) {\n  let className = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : undefined;\n  let idName = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : undefined;\n  if (!className && idName) {\n    var _document$getElementB, _document$getElementB2;\n    (_document$getElementB = document.getElementById(idName)) === null || _document$getElementB === void 0 || _document$getElementB.removeEventListener(eventNMame, instanse);\n    (_document$getElementB2 = document.getElementById(idName)) === null || _document$getElementB2 === void 0 || _document$getElementB2.addEventListener(eventNMame, instanse);\n    return;\n  } else if (className && !idName) {\n    document.getElementsByClassName(className)[0].removeEventListener(eventNMame, instanse);\n    document.getElementsByClassName(className)[0].addEventListener(eventNMame, instanse);\n    return;\n  }\n  return;\n}\n\n//# sourceURL=webpack://ads/./src/scripts/handleRequsetReceiveAd.ts?");

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
/******/ __webpack_require__.O(0, ["shared"], () => (__webpack_exec__("./src/ads/index.ts")));
/******/ var __webpack_exports__ = __webpack_require__.O();
/******/ }
]);