import React from 'react';
import { Link } from 'react-router-dom';
import img from '../../../public/logo.svg';
import icon from '../../../public/logout.svg';
import HeaderStyles from '../../assets/styles/header.module.scss';

interface HeaderProps {}

export const Header: React.FC<HeaderProps> = () => {
  return (
    <>
      <div className={HeaderStyles.header}>
        <div className={HeaderStyles.content}>
          <img src={img} className={HeaderStyles.logo} />
          <div className={HeaderStyles.group}>
            <Link to='/user/:id'>Отчеты</Link>
            <Link to='/create'>Создать график</Link>
            <div className={HeaderStyles.logout}>
              <Link to='/login'>Выйти</Link>
              <img src={icon} width={25} />
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
