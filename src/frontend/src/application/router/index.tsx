import '@/assets/styles/base.css';
import { PageLayout } from '@/components/page-layout';
import { Homepage, SignIn } from '@/pages';
import { CreateGraf } from '@/pages/create-graf';
import { UserProfile } from '@/pages/user-profile';

import { Route, Routes } from 'react-router-dom';

export const AppRouter = () => {
  return (
    <PageLayout>
      <Routes>
        <Route key={'statistic'} element={<SignIn />} path='/login' />
        <Route key={'home'} element={<Homepage />} path='/' />
        <Route key={'create'} element={<CreateGraf />} path='/create' />
        <Route key={'user'} element={<UserProfile />} path='/user/:id' />
      </Routes>
    </PageLayout>
  );
};