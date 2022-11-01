import { useEffect } from 'react';

import {
  useDispatch,
  useSelector
} from 'react-redux';

import {
  Form,
  Input,
  Button,
  Typography,
  notification
} from 'antd';

import {
  MailOutlined,
  LockOutlined,
  LoadingOutlined
} from '@ant-design/icons';

import {
  login,
  setLoginFlag,
  removeError
} from '../redux/slices/user';

const {
  useForm,
  Item: FormItem
} = Form;
const { Password } = Input;
const { Text } = Typography;

const formStyle = {
  margin: '20px 0'
};

const inputStyle = {
  borderRadius: '5px'
};

const iconStyle = {
  marginRight: '10px'
};

const buttonStyle = {
  width: '100%'
};

const LoginForm = () => {
  const dispatch = useDispatch();
  const loading = useSelector(state => state.user.loading);
  const loginFlag = useSelector(state => state.user.loginFlag);
  const userError= useSelector(state => state.user.error);
  const [form] = useForm();

  useEffect(() => {
    if (loginFlag) {
      form.resetFields()
      notification.success({
        message: '登入成功',
      })
      dispatch(setLoginFlag(false))
    }
  }, [loginFlag, dispatch, form]);

  const onFinish = (values) => {
    dispatch(login(values));
    dispatch(removeError());
  };

  return (
    <Form
      layout="vertical"
      style={formStyle}
      form={form}
      onFinish={onFinish}>
      { userError && (<Text type="danger">{userError.message}</Text>)}
      <FormItem
        name="email"
        rules={[{ required: true, message: '請輸入電子信箱' }]}>
        <Input
          size="large"
          placeholder="電子信箱"
          style={{
            ...inputStyle,
            marginTop: '5px',
          }}
          prefix={<MailOutlined style={iconStyle}/>}/>
      </FormItem>

      <FormItem
        name="password"
        rules={[{ required: true, message: '請輸入密碼' }]}>
        <Password
          size="large"
          placeholder="密碼"
          style={inputStyle}
          prefix={<LockOutlined style={iconStyle}/>} />
      </FormItem>
      <FormItem style={{ marginBottom: '10px' }}>
        <Button
          size='large'
          type="primary"
          htmlType="submit"
          style={buttonStyle}>
          {loading ? <LoadingOutlined /> : '登入'}
        </Button>
      </FormItem>
      <Text type="secondary">還沒有帳號嗎，快
        <Button type="link" href="/registry" style={{ padding: 0 }}>加入我們</Button>
      </Text>
    </Form>
  )
};

export default LoginForm;