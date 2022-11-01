import { Outlet } from 'react-router-dom';
//@antd
import { Layout } from 'antd';

const { Header, Content } = Layout;

const headerStyle = {
  backgroundColor: '#FFF'
};

const LogoOnlyLayout = () => {
  return (
    <Layout>
      <Header className='logo-only-layout' style={headerStyle}>
        DATE WITH ME
      </Header>
      <Content >
        <Outlet />
      </Content>
    </Layout>
  );
};

export default LogoOnlyLayout