import moment from 'moment'

export const filterEmptyParams = (params, paramskeys) => {
  const paramsTmp = {}
  Object.keys(params).forEach((key) => {
    if (paramskeys.indexOf(key) === -1) {
      return
    }
    if (params[key]) {
      paramsTmp[key] = params[key]
    }
  })
  return params
};

export const formatTime = (time) => 
  moment(time).format('YYYY/MM/DD HH:mm:ss');