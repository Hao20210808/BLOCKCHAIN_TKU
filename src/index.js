import React from 'react';
import * as ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';

import { Provider } from 'react-redux';
import store from './redux/store';
import { setToken } from './redux/slices/user';

import App from './App';

import reportWebVitals from './reportWebVitals';
import initAxios from './config/initAxios';

import 'antd/dist/antd.variable.min.css';


const token = localStorage.getItem('token')
if (token) {
    store.dispatch(setToken(token))
}
initAxios(store);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <HelmetProvider>
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </HelmetProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
