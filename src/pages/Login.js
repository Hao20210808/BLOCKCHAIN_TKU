import { Layout, Typography } from 'antd';

import Page from '../components/Page';

import LoginForm from '../sections/LoginForm';

const { Content } = Layout
const { Title, Text } = Typography;

const constentStyle = {
  width: '100%',
  maxWidth: '600px',
  minWidth: '480px',
  height: 'calc(100vh - 64px)',
  margin: '0 auto',
  padding: '100px 40px',
  backgroundColor: '#FFF'
}

const Login = () => (
  <Page title="登入">
    <Content style={constentStyle}>
      <Title>登入</Title>
      <Text type="secondary">Hi, Welcome</Text>
      <LoginForm />
    </Content>
  </Page>
);

export default Login;
