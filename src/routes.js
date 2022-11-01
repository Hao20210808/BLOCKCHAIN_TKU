import { Navigate, useRoutes } from 'react-router-dom';
// sections
import RequireAuth from './sections/RequireAuth';

// layouts
import LogoOnlyLayout from './layouts/LogoOnlyLayout';

import Login from './pages/Login';
import Registry from './pages/Registry';
import NotFound from './pages/Page404';

// ----------------------------------------------------------------------


export default function Router() {
  const withAuth = (component) => (
    <RequireAuth>
      {component}
    </RequireAuth>
  );

  return useRoutes([
    {
      path: '/',
      element: <LogoOnlyLayout />,
      children: [
        { path: 'login', element: withAuth(<Login />) },
        { path: 'registry', element: withAuth(<Registry />) },
        { path: '404', element: <NotFound /> },
        { path: '*', element: <Navigate to="/404" /> },
      ],
    }, {
      path: '*',
      element: <Navigate to="/404" replace />
    }
  ]);
}
