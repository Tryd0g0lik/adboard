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

/***/ "./src/index.ts":
/*!**********************!*\
  !*** ./src/index.ts ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _styles_messenger_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./styles/messenger.css */ \"./src/styles/messenger.css\");\n/* harmony import */ var _styles_style_scss__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./styles/style.scss */ \"./src/styles/style.scss\");\n/* harmony import */ var _scripts_index__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./scripts/index */ \"./src/scripts/index.ts\");\n\n\n\n\n//# sourceURL=webpack://ads/./src/index.ts?");

/***/ }),

/***/ "./src/scripts/handlers/HandlerFormAd/hendlerRequst.ts":
/*!*************************************************************!*\
  !*** ./src/scripts/handlers/HandlerFormAd/hendlerRequst.ts ***!
  \*************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerRequestAddAd: () => (/* binding */ asyncHandlerRequestAddAd)\n/* harmony export */ });\n/**\r\n * src\\sripts\\handlers\\HandlerFormAd\\hendlerRequst.ts\r\n */\n\n/**\r\n * This make the post-request to server, it adds the one a new Ad.\r\n * @param event Mouse click.\r\n * @returns boolean or AdLine\r\n */\nconst asyncHandlerRequestAddAd = async event => {\n  const URL_HOST_FOR_API = \"http://127.0.0.1:8000\" || 0;\n  event.stopPropagation();\n\n  // GET SUBMIT HTML\n  if (event.target && event.target.tagName.toLowerCase() !== \"button\") {\n    return false;\n  }\n  console.log(\"START FORM's HANDLER OF AD\");\n  event.preventDefault();\n  // GET FORM HTML FOR AD\n  const currenttarget = event.currentTarget;\n  if (currenttarget && currenttarget.tagName.toLowerCase() !== \"form\") {\n    return false;\n  }\n  // GET DATA OF FORM\n  const dataF0rm = new FormData(currenttarget);\n  try {\n    // REQUEST TO SERVER AND SEND AD's DATA OF FORM\n    console.log(\" REQUEST TO SERVER AND SEND AD's DATA OF FORM;\");\n    const response = await fetch(\"\".concat(URL_HOST_FOR_API, \"/api/v1/ads/\"), {\n      method: \"POST\",\n      body: dataF0rm\n    });\n    if (!response.ok) {\n      console.log(\"RESPONSE OF AD NOT Ok\");\n      return false;\n    }\n    // CLEANING THE BODY OF FORM HTML\n    currenttarget.querySelectorAll(\"input\").forEach(input => {\n      input.value = \"\";\n    });\n    currenttarget.querySelectorAll(\"textarea\").forEach(textarea => {\n      textarea.value = \"\";\n    });\n    //  GET JSON DATA\n    const body = await response.json();\n    // RESPONCE OF AD IS OK\n    console.log(\"RESPONCE OF AD IS OK: \".concat(body));\n    const data = JSON.parse(body);\n    return data;\n  } catch (error) {\n    console.log(\"AD REQUEST ERROR => \".concat(error));\n    return false;\n  }\n};\n\n//# sourceURL=webpack://ads/./src/scripts/handlers/HandlerFormAd/hendlerRequst.ts?");

/***/ }),

/***/ "./src/scripts/handlers/HandlerFormAd/index.ts":
/*!*****************************************************!*\
  !*** ./src/scripts/handlers/HandlerFormAd/index.ts ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   formPage: () => (/* binding */ formPage)\n/* harmony export */ });\n/* harmony import */ var src_scripts_handlers_HandlerFormImg__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/scripts/handlers/HandlerFormImg */ \"./src/scripts/handlers/HandlerFormImg/index.ts\");\n/* harmony import */ var _handlersAdsCollection_handlerReceiveNewAd__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../handlersAdsCollection/handlerReceiveNewAd */ \"./src/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts\");\n/* harmony import */ var _hendlerRequst__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./hendlerRequst */ \"./src/scripts/handlers/HandlerFormAd/hendlerRequst.ts\");\n/**\r\n * src\\sripts\\handlers\\HandlerFormAd\\index.ts\r\n */\n\n\n\n\n/**\r\n * This function for add the two listens to the form, the first is for send ads to server, and the second is for send image file to server.\r\n * @returns boolean.\r\n */\nfunction formPage() {\n  // ADS FORM\n  const formHTML = document.querySelector(\".form form\");\n  // IMAGE FILE FORM\n  const formImageFileHTML = document.querySelector(\".form form.ads-form__full-image-file\");\n  if (!formHTML) {\n    console.log(\"Somewing that frong! Invalid form.\");\n    return false;\n  } else {\n    const formHTMLCopy = formHTML;\n    // ----- EVENT ONCLICK FOR ADS -----\n    formHTMLCopy.onclick = async e => {\n      const dataBoolJson = await (0,_hendlerRequst__WEBPACK_IMPORTED_MODULE_2__.asyncHandlerRequestAddAd)(e);\n      if ((typeof dataBoolJson).toLowerCase() === 'boolean') {\n        return false;\n      }\n      const dataJson = dataBoolJson;\n      // ONE AD  SEND TO PUBLIC IN WEB-PAGE\n      (0,_handlersAdsCollection_handlerReceiveNewAd__WEBPACK_IMPORTED_MODULE_1__.asyncHandlerReceivesData)(dataJson.data);\n      return true;\n    };\n  }\n  if (!formImageFileHTML) {\n    console.log(\"Somewing that frong! Invalid form.\");\n    return false;\n  } else {\n    const formHTMLCopy = formImageFileHTML;\n    //----- EVENT ONCLICK FOR IMAGE -----\n    formHTMLCopy.onclick = async e => {\n      const responce = await (0,src_scripts_handlers_HandlerFormImg__WEBPACK_IMPORTED_MODULE_0__.asyncHandlerRequestAddImage)(e);\n      if (!responce) {\n        console.log(\"RESPONSE OF SEND IMAGE IS NOT OK\");\n        return false;\n      }\n      return true;\n    };\n  }\n  return true;\n}\n\n//# sourceURL=webpack://ads/./src/scripts/handlers/HandlerFormAd/index.ts?");

/***/ }),

/***/ "./src/scripts/handlers/HandlerFormImg/index.ts":
/*!******************************************************!*\
  !*** ./src/scripts/handlers/HandlerFormImg/index.ts ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerRequestAddImage: () => (/* binding */ asyncHandlerRequestAddImage)\n/* harmony export */ });\n/**\r\n * src\\sripts\\handlers\\HandlerFormImg\\index.ts\r\n */\nconst URL_HOST_FOR_API = \"http://127.0.0.1:8000\" || 0;\n/**\r\n * This handler of post request for add only one an image to server.\r\n * @param event handler of clik by button of form. This form load the image to server.\r\n * @returns  AdLine or boolean\r\n */\nconst asyncHandlerRequestAddImage = async event => {\n  event.stopPropagation();\n\n  // GET SUBMIT HTML\n  if (event.target && event.target.tagName.toLowerCase() !== \"button\") {\n    return false;\n  }\n  event.preventDefault();\n  // GET FORM HTML\n  const currenttarget = event.currentTarget;\n  if (currenttarget && currenttarget.tagName.toLowerCase() !== \"form\") {\n    return false;\n  }\n  const dataF0rm = new FormData(currenttarget);\n  // REQUEST TO SERVER AND SEND FILE IMAGE\n  try {\n    const response = await fetch(\"\".concat(URL_HOST_FOR_API, \"/api/v1/image/\"), {\n      method: \"POST\",\n      body: dataF0rm\n    });\n    if (!response.ok) {\n      return false;\n    }\n    // RESPONCE IS OK\n    const body = await response.json();\n    console.log(\"SERVER: \".concat(body));\n    return body;\n  } catch (error) {\n    console.log(\"Request of FIleImage to server Error => \".concat(error));\n    return false;\n  }\n};\n\n//# sourceURL=webpack://ads/./src/scripts/handlers/HandlerFormImg/index.ts?");

/***/ }),

/***/ "./src/scripts/handlers/handlerSingleAd/handleRequsetReceiveAd.ts":
/*!************************************************************************!*\
  !*** ./src/scripts/handlers/handlerSingleAd/handleRequsetReceiveAd.ts ***!
  \************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncGetListenerEvent: () => (/* binding */ asyncGetListenerEvent),\n/* harmony export */   asyncHandlerOneAdPublic: () => (/* binding */ asyncHandlerOneAdPublic)\n/* harmony export */ });\n/**\r\n * src\\scripts\\handlers\\handlerSingleAd\\handleRequsetReceiveAd.ts\r\n */\n\nconst URL_HOST_FOR_API = \"http://127.0.0.1:8000\" || 0;\nfunction handlerSubmitGetIdFroHTML(event) {\n  var _target$parentElement;\n  if (!(event.target instanceof HTMLElement)) {\n    return;\n  }\n  if (event.target.tagName.toLowerCase() !== \"button\") {\n    return;\n  }\n  event.stopPropagation();\n  event.preventDefault();\n  const target = event.target;\n  const liParantHtml = (_target$parentElement = target.parentElement) === null || _target$parentElement === void 0 || (_target$parentElement = _target$parentElement.parentElement) === null || _target$parentElement === void 0 ? void 0 : _target$parentElement.parentElement;\n  if ((liParantHtml === null || liParantHtml === void 0 ? void 0 : liParantHtml.tagName).toLowerCase() !== \"li\") {\n    console.error(\"The tag 'LI' is invalid!\");\n    return;\n  }\n  const getId = liParantHtml.hasAttribute('data-ad') ? liParantHtml.getAttribute('data-ad') : undefined;\n  if (!getId) {\n    console.error(\"The 'no id' is invalid!\");\n    return;\n  }\n  console.warn(\"THe ID of Ad is Ok.\");\n  return getId;\n}\n\n/**\r\n * This function is called when you click on the button 'submit' and get the index of the Ad.\\\r\n * Then, relocation to the page of the public Ad (http://< HOST >/ad/id/) .\r\n * @param event of click.\r\n * @returns  Promise<void>\r\n */\nasync function asyncHandlerOneAdPublic(event) {\n  // GET INDEX OF Ad FROM HTML-ELEMENT\n  const data = handlerSubmitGetIdFroHTML(event);\n  if (!data) {\n    console.warn(\"The index's data of Ad is invalid!\");\n    return;\n  }\n  window.location.href = \"\".concat(URL_HOST_FOR_API, \"/ad/\").concat(data, \"/\");\n}\n\n/**\r\n * Here, to the entrypoint accepting the 'instance' and 'className' or 'idName' (only one) of HTML-element. \\\r\n * It (html-element wich has the'className' or 'idName')\\\r\n * will receive 'instance' (a callback function), this function will be handle the events. \r\n * @param instanse: async callback c this a function that handle event 'click' by submit\r\n * @param className: string. Default value undefined. \r\n * @param idName : string. Default value undefined.\r\n * @returns void.\r\n */\nasync function asyncGetListenerEvent(instanse) {\n  let className = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : undefined;\n  let idName = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : undefined;\n  if (!className && idName) {\n    var _document$getElementB, _document$getElementB2;\n    (_document$getElementB = document.getElementById(idName)) === null || _document$getElementB === void 0 || _document$getElementB.removeEventListener(\"click\", instanse);\n    (_document$getElementB2 = document.getElementById(idName)) === null || _document$getElementB2 === void 0 || _document$getElementB2.addEventListener(\"click\", instanse);\n    return;\n  } else if (className && !idName) {\n    document.getElementsByClassName(className)[0].removeEventListener(\"click\", instanse);\n    document.getElementsByClassName(className)[0].addEventListener(\"click\", instanse);\n    return;\n  }\n  return;\n}\n\n//# sourceURL=webpack://ads/./src/scripts/handlers/handlerSingleAd/handleRequsetReceiveAd.ts?");

/***/ }),

/***/ "./src/scripts/handlers/handlerSingleAd/handlerGetOneAd.ts":
/*!*****************************************************************!*\
  !*** ./src/scripts/handlers/handlerSingleAd/handlerGetOneAd.ts ***!
  \*****************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerRequestGetOneAd: () => (/* binding */ asyncHandlerRequestGetOneAd)\n/* harmony export */ });\n/**\r\n * src\\scripts\\handlers\\handlerSingleAd\\handlerGetOneAd.ts\r\n */\n\n/**\r\n * @param: pathname string. This is the path of api.  Exemple - '/api/ad/one/'.\r\n * @param index type stryng. This is the indes of the ad. It is an one data line from server.\r\n * @returns json data (`{ data: AdLine[] `)\r\n */\nasync function asyncHandlerRequestGetOneAd(pathname, index) {\n  try {\n    const response = await fetch(\"\".concat(pathname).concat(index), {\n      method: 'GET',\n      headers: {\n        'Content-Type': 'application/json'\n      }\n    });\n    if (!response.ok) {\n      console.error(\"The 'error' of GET: \".concat(response.statusText));\n      return;\n    }\n    const data = await response.json();\n    const dataJson = JSON.parse(data);\n    return dataJson;\n  } catch (err) {\n    console.error(new Error(\"The 'index' ERROR: \" + err));\n  }\n  return;\n}\n\n//# sourceURL=webpack://ads/./src/scripts/handlers/handlerSingleAd/handlerGetOneAd.ts?");

/***/ }),

/***/ "./src/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts":
/*!***************************************************************************!*\
  !*** ./src/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts ***!
  \***************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerReceivesData: () => (/* binding */ asyncHandlerReceivesData)\n/* harmony export */ });\n/* harmony import */ var src_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/scripts/services/taskCreateOneElement */ \"./src/scripts/services/taskCreateOneElement.ts\");\n/**\r\n * src\\sripts\\handlers\\handlersAdsCollection\\handlerReceiveNewAd.ts\r\n */\n\n\n/**\r\n * This handler for publicate the one new ad or list of ads's collection in web-page.\r\n * @param content Adline's or AdLinesCollection data type. Default value is undefined.\r\n * @returns Promise boolean\r\n */\nasync function asyncHandlerReceivesData() {\n  let content = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : undefined;\n  if (!content) {\n    /**\r\n     * Дополнителььная функция request для запроса get получить  список ads\r\n     */\n    null;\n    return true;\n  }\n  const collectionsHTML = document.querySelector(\"#ads-collections ul.ads-views\");\n  if (!collectionsHTML) {\n    console.log(\"INVALID 'ads-collections'\");\n    false;\n  } else {\n    // RECEIVING HTML CONTENT FROM SERVER's/API's DATA\n    if (!Array.isArray(content)) {\n      (0,src_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(collectionsHTML, content);\n    } else content.forEach(item => {\n      (0,src_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(collectionsHTML, item);\n    });\n  }\n  // ulHtml\n  return true;\n}\n;\n\n//# sourceURL=webpack://ads/./src/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts?");

/***/ }),

/***/ "./src/scripts/handlers/handlersAdsCollection/handlerRequestlCollection.ts":
/*!*********************************************************************************!*\
  !*** ./src/scripts/handlers/handlersAdsCollection/handlerRequestlCollection.ts ***!
  \*********************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   asyncHandlerGetAdsCollection: () => (/* binding */ asyncHandlerGetAdsCollection)\n/* harmony export */ });\n/**\r\n * src\\scripts\\handlers\\handlersAdsCollection\\handlerRequestlCollection.ts\r\n * */\nconst URL_HOST_FOR_API = \"http://127.0.0.1:8000\" || 0;\n/**\r\n * This function is download the collection of the ads from server.\r\n * @returns {data: AdLinesCollection} | void\r\n */\nasync function asyncHandlerGetAdsCollection() {\n  try {\n    // REQUEST GET COLLECTION ADS\n    const url = new URL(\"\".concat(URL_HOST_FOR_API, \"/api/v1/ads\"));\n    const response = await fetch(url, {\n      method: \"GET\"\n    });\n    if (!response.ok) {\n      console.error(\"The Ads downloads data invalid!\");\n      return;\n    }\n    // RESEIVING RESPONSE DATA IN JSON TYPE\n    const responseData = await response.json();\n    const data = JSON.parse(responseData);\n    return data;\n  } catch (err) {\n    console.log(\"Error: \".concat(err.message));\n  }\n  return;\n}\n\n//# sourceURL=webpack://ads/./src/scripts/handlers/handlersAdsCollection/handlerRequestlCollection.ts?");

/***/ }),

/***/ "./src/scripts/index.ts":
/*!******************************!*\
  !*** ./src/scripts/index.ts ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _handlers_HandlerFormAd__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./handlers/HandlerFormAd */ \"./src/scripts/handlers/HandlerFormAd/index.ts\");\n/* harmony import */ var src_scripts_services_taskPublicAllAd__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! src/scripts/services/taskPublicAllAd */ \"./src/scripts/services/taskPublicAllAd.ts\");\n/* harmony import */ var src_scripts_handlers_handlerSingleAd_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/scripts/handlers/handlerSingleAd/handleRequsetReceiveAd */ \"./src/scripts/handlers/handlerSingleAd/handleRequsetReceiveAd.ts\");\n/* harmony import */ var _services_taskPublicOnAd__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./services/taskPublicOnAd */ \"./src/scripts/services/taskPublicOnAd.ts\");\n/**\r\n * src\\scripts\\index.ts\r\n */\n\n\n\n\n// LISTENER CLICK BY FORM's SUBMIT BUTTOM\n\ndocument.removeEventListener(\"DOMContentLoaded\", () => {\n  (0,_handlers_HandlerFormAd__WEBPACK_IMPORTED_MODULE_0__.formPage)();\n  // publicAllAd - public all ads in HTML\n  Promise.all([(0,src_scripts_services_taskPublicAllAd__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(), (0,src_scripts_handlers_handlerSingleAd_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_2__.asyncGetListenerEvent)(src_scripts_handlers_handlerSingleAd_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_2__.asyncHandlerOneAdPublic, undefined, undefined), (0,_services_taskPublicOnAd__WEBPACK_IMPORTED_MODULE_3__[\"default\"])()]);\n});\ndocument.addEventListener(\"DOMContentLoaded\", () => {\n  (0,_handlers_HandlerFormAd__WEBPACK_IMPORTED_MODULE_0__.formPage)();\n  // publicAllAd - public all ads in HTML\n  const idName = 'ads-collections';\n  Promise.all([(0,src_scripts_services_taskPublicAllAd__WEBPACK_IMPORTED_MODULE_1__[\"default\"])(), (0,src_scripts_handlers_handlerSingleAd_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_2__.asyncGetListenerEvent)(src_scripts_handlers_handlerSingleAd_handleRequsetReceiveAd__WEBPACK_IMPORTED_MODULE_2__.asyncHandlerOneAdPublic, undefined, idName), (0,_services_taskPublicOnAd__WEBPACK_IMPORTED_MODULE_3__[\"default\"])()]);\n});\n\n//# sourceURL=webpack://ads/./src/scripts/index.ts?");

/***/ }),

/***/ "./src/scripts/services/taskCreateOneElement.ts":
/*!******************************************************!*\
  !*** ./src/scripts/services/taskCreateOneElement.ts ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/**\r\n * src\\scripts\\services\\createOneElement.ts\r\n */\n\n/**\r\n * \r\n * @param instance HTMLElement This is main BOX for inserting by one line of ads\r\n * @param content AdLine's type. It is object (or json data) from server/api\r\n * @returns void\r\n  */\nconst teskInsertOneAd = (instance, content) => {\n  // CREATE THE PARENT CONTEXT's BOX \n  const newLineHtml = document.createElement('li');\n  newLineHtml.className = 'ad-view';\n  newLineHtml.dataset.ad = \"\".concat(content.id);\n\n  // CREATE CONTENT CONTAINER\n  const viewContentHTml = document.createElement('div');\n  viewContentHTml.className = 'ad-view-container';\n  // CREATE TITLE\n  const titleAdHtml = document.createElement('div');\n  titleAdHtml.className = 'ad-view-title';\n  const titleHeading = document.createElement('h2');\n  titleHeading.textContent = content.title;\n  titleAdHtml.append(titleHeading);\n\n  // CREATE DESCRIPTION\n  const contextAdHtml = document.createElement('div');\n  contextAdHtml.className = 'ad-view-content';\n  contextAdHtml.textContent = content.description;\n\n  // CREATE FOOTER\n  const viewFooterHtml = document.createElement('div');\n  viewFooterHtml.className = 'ad-view-footer';\n  const button = document.createElement('button');\n  button.type = 'submit';\n  button.className = 'ad-moving btn btn-primary';\n  button.textContent = 'Перейти';\n  viewFooterHtml.append(button);\n\n  // ASSEMBLE ALL PARTS\n  viewContentHTml.append(titleAdHtml);\n  viewContentHTml.append(contextAdHtml);\n  viewContentHTml.append(viewFooterHtml);\n  newLineHtml.append(viewContentHTml);\n\n  // PUBLICATION TO WEB PAGE\n  instance.append(newLineHtml);\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (teskInsertOneAd);\n\n//# sourceURL=webpack://ads/./src/scripts/services/taskCreateOneElement.ts?");

/***/ }),

/***/ "./src/scripts/services/taskPublicAllAd.ts":
/*!*************************************************!*\
  !*** ./src/scripts/services/taskPublicAllAd.ts ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var src_scripts_handlers_handlersAdsCollection_handlerRequestlCollection__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/scripts/handlers/handlersAdsCollection/handlerRequestlCollection */ \"./src/scripts/handlers/handlersAdsCollection/handlerRequestlCollection.ts\");\n/* harmony import */ var _handlers_handlersAdsCollection_handlerReceiveNewAd__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../handlers/handlersAdsCollection/handlerReceiveNewAd */ \"./src/scripts/handlers/handlersAdsCollection/handlerReceiveNewAd.ts\");\n/**\r\n * src\\scripts\\services\\taskPublicAllAd.ts\r\n */\n\n\n\n/**\r\n * This function is responsible for requesting the collection of ads and publishing them in the HTML.\r\n * @returns void\r\n */\nconst asyncPublicAllAd = async () => {\n  // REQUEST GET COLLECTION ADS\n  const response = await (0,src_scripts_handlers_handlersAdsCollection_handlerRequestlCollection__WEBPACK_IMPORTED_MODULE_0__.asyncHandlerGetAdsCollection)();\n  if (!response) {\n    console.error(\"Error fetching ads!\");\n    return;\n  }\n  // PUBLICT COLLECTION OF ADS ON HTML\n  await (0,_handlers_handlersAdsCollection_handlerReceiveNewAd__WEBPACK_IMPORTED_MODULE_1__.asyncHandlerReceivesData)(response[\"data\"]);\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (asyncPublicAllAd);\n\n//# sourceURL=webpack://ads/./src/scripts/services/taskPublicAllAd.ts?");

/***/ }),

/***/ "./src/scripts/services/taskPublicOnAd.ts":
/*!************************************************!*\
  !*** ./src/scripts/services/taskPublicOnAd.ts ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var src_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! src/scripts/services/taskCreateOneElement */ \"./src/scripts/services/taskCreateOneElement.ts\");\n/* harmony import */ var src_scripts_handlers_handlerSingleAd_handlerGetOneAd__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! src/scripts/handlers/handlerSingleAd/handlerGetOneAd */ \"./src/scripts/handlers/handlerSingleAd/handlerGetOneAd.ts\");\n/**\r\n * src\\scripts\\services\\taskPublicOnAd.ts\r\n */\n\n\n\nconst asyncTaskPublicOneAd = async () => {\n  // GET ID OF AD FROM THE URL\n  const pathname = window.location.pathname;\n  const index = pathname.split(\"/\")[2];\n  // GET DATA OF AD FROM THE SERVER\n  const response = await (0,src_scripts_handlers_handlerSingleAd_handlerGetOneAd__WEBPACK_IMPORTED_MODULE_1__.asyncHandlerRequestGetOneAd)('/api/v1/ads/', index);\n  if (!response) {\n    console.error(\"The received data from server is invalid!\");\n    return;\n  }\n  const sectionHtml = document.getElementById(\"ad-page-container\");\n  if (!sectionHtml) {\n    console.error(\"The section HTML is invalid!\");\n    return;\n  }\n  // PUBLIC AD ON AD PAGE\n  (0,src_scripts_services_taskCreateOneElement__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(sectionHtml, response.data[0]);\n  const buttonHtml = document.querySelector(\".ad-view-footer button\");\n  if (!buttonHtml) {\n    return;\n  }\n  buttonHtml.remove();\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (asyncTaskPublicOneAd);\n\n//# sourceURL=webpack://ads/./src/scripts/services/taskPublicOnAd.ts?");

/***/ }),

/***/ "./src/styles/messenger.css":
/*!**********************************!*\
  !*** ./src/styles/messenger.css ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n// extracted by mini-css-extract-plugin\n\n\n//# sourceURL=webpack://ads/./src/styles/messenger.css?");

/***/ }),

/***/ "./src/styles/style.scss":
/*!*******************************!*\
  !*** ./src/styles/style.scss ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n// extracted by mini-css-extract-plugin\n\n\n//# sourceURL=webpack://ads/./src/styles/style.scss?");

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ __webpack_require__.O(0, ["shared"], () => (__webpack_exec__("./src/index.ts")));
/******/ var __webpack_exports__ = __webpack_require__.O();
/******/ }
]);