import React from 'react';
import img from '../../../public/logo.svg';
import HeaderStyles from '../../assets/styles/header.module.scss';

interface HeaderProps {}

export const Header: React.FC<HeaderProps> = () => {
  return (
    <>
      <div className={HeaderStyles.header}>
        <div className={HeaderStyles.content}>
          <img src={img} className={HeaderStyles.logo} />
          <div className={HeaderStyles.group}>
            <a>Отчеты</a>
            <a>Новый отчет</a>
            <a>График</a>
            <a>Выйти</a>
          </div>
        </div>
      </div>
    </>
  );
};
