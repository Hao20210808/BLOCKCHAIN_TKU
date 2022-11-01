import { useNavigate } from 'react-router-dom';
import { Layout, Typography, Image, Button } from 'antd';
import { LeftOutlined } from '@ant-design/icons';

import Page from '../components/Page';
import page404Img from '../assets/img/page404.svg';


const { Content } = Layout
const { Title, Text } = Typography;

const constentStyle = {
  display: 'flex',
  flexDirection: 'column',
  width: '100%',
  maxWidth: '600px',
  minWidth: '480px',
  height: 'calc(100vh - 64px)',
  margin: '0 auto',
  padding: '60px 40px',
  backgroundColor: '#FFF'
}

const imageStyle = {
  marginTop: '20px'
}

const buttonStyle = {
  margin: '10px auto'
}

const Login = () => {
  const navigator = useNavigate();
  const handleClick = () => {
    navigator('/dashboard', { replace: true });
  };
  return(
    <Page title="404找不到頁面">
      <Content style={constentStyle}>
        <Title>抱歉，找不到頁面。</Title>
        <Text type="secondary">抱歉，我們無法找到您指定的頁面，請您確認URL沒有任何錯誤。</Text>
        <Image
          style={imageStyle}
          src={page404Img}
          preview={false} />
        <Button
          type="primary"
          icon={<LeftOutlined />} 
          style={buttonStyle}
          onClick={handleClick}>
          返回首頁
        </Button>
      </Content>
    </Page>
  )
};

export default Login;
