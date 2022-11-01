import { Outlet } from 'react-router-dom';
//@antd
import { Layout } from 'antd';

import DashBoardSider from './DashBoardSider';
import DashBoardHeader from './DashBoardHeader';

const { Content } = Layout;

const DashBoardLayout = () => {
  return (
    <Layout>
      <DashBoardSider />
      <Layout>
        <DashBoardHeader />
        <Content>
          <Outlet />
        </Content>
      </Layout>
    </Layout>
  );
};

export default DashBoardLayout;