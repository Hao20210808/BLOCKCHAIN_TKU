import PropTypes from 'prop-types';
import { ConfigProvider } from 'antd';

import './theme.scss';

ConfigProvider.config({
  theme: {
    primaryColor: '#faad14',
  },
});

const ThemeProvider = ({ children, ...props }) => {
  return (
    <ConfigProvider {...props}>
      {children}
    </ConfigProvider>
  )
}

ThemeProvider.prototype = {
  children: PropTypes.node,
  props: PropTypes.object
}

export default ThemeProvider