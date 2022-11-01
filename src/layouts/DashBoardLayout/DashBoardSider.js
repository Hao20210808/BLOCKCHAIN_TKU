import { useState } from 'react';

import {
  useNavigate,
  useLocation,
} from 'react-router-dom';

import { Layout, Menu } from 'antd';

import {
  TeamOutlined,
  DribbbleOutlined,
  DollarOutlined
} from '@ant-design/icons';

import Logo from '../../components/Logo';

const { Sider, Header } = Layout;

const siderStyle = {
  minHeight: '100vh',
  borderRight: '1px dashed var(--ant-primary-color)',
  backgroundColor: '#FFF'
};

const navItems = [
  {
    label: '會員管理',
    key: '/member',
    icon: <TeamOutlined />,
    children: [
      {
        label: '總代理列表',
        key: '/member/super-agents',
      }, {
        label: '代理列表',
        key: '/member/agents',
      }, {
        label: '玩家列表',
        key: '/member/players',
      }
    ]
  }, {
    label: '彩票管理',
    key: '/lottery',
    icon: <DribbbleOutlined />,
    children: [
      {
        label: '注單列表',
        key: '/lottery/orders',
      }, {
        label: '限額列表',
        key: '/lottery/limits',
      }, {
        label: '風控列表',
        key: '/lottery/monitors',
      },
    ]
  },  {
    label: '帳務管理',
    key: '/payment',
    icon: <DollarOutlined />,
    children: [
      {
        label: '總代理帳務列表',
        key: '/payment/super-agents',
      }, {
        label: '代理帳務列表',
        key: '/payment/agents',
      }, {
        label: '玩家帳務列表',
        key: '/payment/players',
      }
    ]
  },
];

const DashBoardSider = () => {
  const { pathname } = useLocation();
  const navigator = useNavigate();
  const [openKeys, setOpenKeys] = useState([`/${pathname.split('/')[2]}`]);
  const [selectedKeys, setSelectedKeys] = useState([pathname === '/dashboard' ? '/member/super-agents' : pathname.replace('/dashboard', '') ]); 

  const handleOpenChange = (keys) => {
    setOpenKeys([keys[1]]);
  }

  const handleClick = (e) => {
    if (pathname.replace('/dashboard', '') !== e.key) {
      setSelectedKeys([e.key]);
      navigator(`/dashboard${e.key}`, { replace: true });
    }
  };
  
  return (
    <Sider style={siderStyle}>
      <Layout>
        <Header>
          <Logo />
        </Header>
      </Layout>
      <Menu
        mode="inline"
        items={navItems}
        openKeys={openKeys}
        selectedKeys={selectedKeys}
        onClick={handleClick}
        onOpenChange={handleOpenChange}
      />
    </Sider>
  );
};

export default DashBoardSider;