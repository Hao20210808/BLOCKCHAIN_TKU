import { Layout, Typography } from 'antd';

import Page from '../components/Page';

import RegistryForm from '../sections/RegistryForm';

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
  <Page title="註冊">
    <Content style={constentStyle}>
      <Title>註冊</Title>
      <Text type="secondary">Join Us</Text>
      <RegistryForm />
    </Content>
  </Page>
);

export default Login;