import { RouterModule, Routes } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';

import { AddCommentComponent } from './add-comment/add-comment.component';

export const AppRoutes: Routes = [
	{ path: '', component: AddCommentComponent },
];

export const ROUTING: ModuleWithProviders<RouterModule> = RouterModule.forRoot(AppRoutes); 