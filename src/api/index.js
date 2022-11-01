import axios from 'axios';

export const systemApi = {
  user: {
    login: (data) => axios.post('/api/login', data),
    registry: (data) => axios.post('/api/registry', data),
  }
};
