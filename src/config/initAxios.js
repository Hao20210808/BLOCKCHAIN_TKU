import axios from 'axios';
import { nanoid } from 'nanoid';

import { removeToken } from '../redux/slices/user'

const connectSource = new Map();

export const cancelAllRequest = () => {
  connectSource.forEach(el => {
    el.cancel('reject')
  })
  connectSource.clear()
}

const initAxios = (store) => {
  axios.interceptors.request.use((config) => {

    const source = axios.CancelToken.source();
    const id = nanoid();
    connectSource.set(id, source);
    
    const state = store.getState();
    const { token } = state.user;
    if (token) {
      config.headers.token = token;
    }
    return config;
  })
  axios.interceptors.response.use((res) => {
    return res.data
  }, (error) => {
    if (error.message === 'reject') {
      return Promise.reject({
        message: null,
      });
    }
  
    if (!error.response) {
      return Promise.reject({
        message: '抱歉，系統錯誤'
      });
    }

    if (!error.response.data.msg) {
      return Promise.reject({
        message: '抱歉，系統錯誤'
      });
    } 

    if ([
      '登出'
    ].indexOf(error.response.data.msg) !== -1) {
      cancelAllRequest()
      store.dispatch(removeToken())
    }

    return Promise.reject({
      message: error.response.data.msg,
    });
  })
}

export default initAxios