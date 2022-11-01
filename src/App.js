// routes
import Router from './routes';
// theme
import ThemeProvider from './theme/index';
import zhTW from 'antd/lib/locale/zh_TW';

// components
import ScrollToTop from './components/ScrollToTop';

function App() {
  return (
    <ThemeProvider locale={zhTW}>
      <ScrollToTop />
      <Router />
    </ThemeProvider>
  );
}

export default App;
