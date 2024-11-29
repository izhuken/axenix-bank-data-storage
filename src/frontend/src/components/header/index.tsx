import { HeaderStyles } from '@/assets';
import React, { useState } from 'react';
import { Link } from 'react-router-dom';

interface HeaderProps {}

const HeaderFc: React.FC<HeaderProps> = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // useEffect(() => {
  //   useAuthentication().then((response) => {
  //     if (!response) return setIsAuthenticated(false);
  //     setIsAuthenticated(true);
  //     return;
  //   });
  // });

  return (
    <header className={HeaderStyles.header}>
      <article className={HeaderStyles.icon}>
        <img src='/dev-lab-icon.svg' alt='icon' />
        <span>DevLab</span>
      </article>
      <article className={HeaderStyles.linkContainer}>
        {isAuthenticated ? (
          <>
            <Link to='/admin'>Админ</Link>
            <Link to='/logout'>Выход</Link>
          </>
        ) : (
          <>
            <Link to='/sign-in'>Вход</Link>
            <Link to='/sign-up'>Регистрация</Link>
          </>
        )}
      </article>
      <article className={HeaderStyles.burger}>
        <img src='/burger.svg' alt='Меню' onClick={() => {}} />
        {/* <BurgerMenu isAuthenticated={isAuthenticated} /> */}
      </article>
    </header>
  );
};

export const Header = React.memo(HeaderFc);
