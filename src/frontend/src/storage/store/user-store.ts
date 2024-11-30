import { User } from '@/entities';
import { makeAutoObservable } from 'mobx';
export class UserStorage {
  user: User | null = null;
  constructor() {
    makeAutoObservable(this);
  }
}
