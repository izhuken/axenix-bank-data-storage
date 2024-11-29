import { themeButton } from '@/lib';
import { Button } from '@chakra-ui/react';
import React from 'react';
import { Link } from 'react-router-dom';

interface ButtonProps {
  title: string;
  disablet: boolean;
}

export const NavButton: React.FC<ButtonProps> = (props) => {
  return (
    <>
      <Button
        fontFamily={'Montserrat'}
        width={200}
        height={60}
        {...themeButton({ variants: 'active' })}
      >
        {<Link to={'users/'}>{props.title}</Link>}
      </Button>
    </>
  );
};
