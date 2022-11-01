import { useEffect } from 'react';

import {
  useNavigate,
} from 'react-router-dom';

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
  LoadingOutlined,
  UserOutlined,
  MobileOutlined
} from '@ant-design/icons';

import {
  registry,
  setRegistryFlag,
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

const RegistryForm = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const loading = useSelector(state => state.user.loading);
  const registryFlag = useSelector(state => state.user.registryFlag);
  const userError= useSelector(state => state.user.error);
  const [form] = useForm();

useEffect(() => {
  if (registryFlag) {
    form.resetFields()
    notification.success({
      message: '註冊成功',
    })
    dispatch(setRegistryFlag(false))
    navigate('/login');
  }
}, [registryFlag, dispatch, form]);


  const onFinish = (values) => {
    dispatch(registry(values));
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
        rules={[
          { required: true, message: '請輸入密碼' },
          {
            validator: async (_, password) => {
              if (password) {
                if (password.length < 8 || password > 16 || !(/^(?!.*[^\x21-\x7e])(?=.*[a-zA-Z])(?=.*\d)/.test(password))) {
                  return Promise.reject(new Error('請輸入8~16位元的數字和英文組合'))
                }
              }
              return Promise.resolve();
            }
          }
        ]}>
        <Password
          size="large"
          placeholder="密碼"
          maxLength={16}
          style={inputStyle}
          prefix={<LockOutlined style={iconStyle}/>} />
      </FormItem>

      <FormItem
        name="comfirmPassword"
        rules={[
          { required: true, message: '請輸入確認密碼' },
          ({ getFieldValue }) => ({
            validator(_, value) {
              if (!value || getFieldValue('password') === value) {
                return Promise.resolve();
              }
              return Promise.reject(new Error('與密碼不相符'));
            },
          }),
        ]}>
        <Password
          size="large"
          placeholder="確認密碼"
          style={inputStyle}
          prefix={<LockOutlined style={iconStyle}/>} />
      </FormItem>

      <FormItem
        name="name"
        rules={[{ required: true, message: '請輸入姓名' }]}>
        <Input
          size="large"
          placeholder="姓名"
          style={inputStyle}
          prefix={<UserOutlined style={iconStyle}/>} />
      </FormItem>

      <FormItem
        name="phone"
        rules={[
          { required: true, message: '請輸入手機號碼' },
          {
            validator: async (_, phone) => {
              if (phone) {
                if (phone.length !== 10 || !(/^\d/.test(phone))) {
                  return Promise.reject(new Error('請輸入正確的手機號碼'))
                }
              }
              return Promise.resolve();
            }
          }
        ]}>
        <Input
          size="large"
          placeholder="手機號碼"
          maxLength={10}
          style={inputStyle}
          prefix={<MobileOutlined style={iconStyle}/>} />
      </FormItem>

      <FormItem style={{ marginBottom: '10px' }}>
        <Button
          size='large'
          type="primary"
          htmlType="submit"
          style={buttonStyle}>
          {loading ? <LoadingOutlined /> : '註冊'}
        </Button>
      </FormItem>

      <Text type="secondary">有帳號了，還不快
        <Button type="link" href="/registry" style={{ padding: 0 }}>登入</Button>
      </Text>
    </Form>
  )
};

export default RegistryForm;