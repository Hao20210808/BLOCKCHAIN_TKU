import { useEffect } from 'react';

import {
  useDispatch,
  useSelector
} from 'react-redux';

import {
  useLocation,
  Navigate,
} from 'react-router-dom';

import {
  getUser
} from '../redux/slices/user';

const RequireAuth = ({ children }) => {
  const dispatch = useDispatch()
  const token = useSelector(state => state.user.token);
  const location = useLocation();

  useEffect(() => {
    if (token) {
      dispatch(getUser());
    }
  }, [token, dispatch]);

  if (['/login', '/registry'].includes(location.pathname) && token) {
    let toPath = '/dashboard';
    if (location.state) {
      toPath = location.state.from.pathname
    }
    return <Navigate to={toPath} replace />;
  }

  if (!['/login', '/registry'].includes(location.pathname)  && !token) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}

export default RequireAuth