import {defineConfig} from '@playwright/test';
export default defineConfig({testDir:'./baseline',use:{baseURL:'http://127.0.0.1:8765'},webServer:{command:'python3 -m http.server 8765 --directory fixture',url:'http://127.0.0.1:8765',reuseExistingServer:false},reporter:'list'});
