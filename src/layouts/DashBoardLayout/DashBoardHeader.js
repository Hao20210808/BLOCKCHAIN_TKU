import { useDispatch, useSelector } from 'react-redux';

import {
  Layout,
  Dropdown,
  Button,
  Menu,
} from 'antd';

import {
  DownOutlined
} from '@ant-design/icons';

import { logout } from '../../redux/slices/user';

const { Header } = Layout;


const DashBoardHeader = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.user.user)

  const handleMenuClick = (e) => {
    if (e.key === 'logout') {
      dispatch(logout());
    }
  }
  const menu = (
    <Menu
      style={{
        width: '100px'
      }}
      onClick={handleMenuClick}
      items={[{
        label: '登出',
        key: 'logout',
      }]} />
  )
  return (
    <Header>
      <Dropdown overlay={menu}>
        <Button style={{ marginLeft: 'auto' }}>
          {user ? user.username : 'unKnown'}
          <DownOutlined />
        </Button>
      </Dropdown>
    </Header>
  );
};

export default DashBoardHeader;