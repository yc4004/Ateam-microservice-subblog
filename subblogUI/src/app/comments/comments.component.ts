import { Component } from '@angular/core';
import { CommentsService } from './comments.service';
import { Comment } from '../models/comment.model';
import { Router } from '@angular/router';

@Component({
  selector: 'comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.css'],
  providers: [CommentsService],
})
export class CommentsComponent {
  public comments: any = [];

  constructor(
    private commentsService: CommentsService,
    private router: Router) {
    // this.comments = new Comments();
  }

  ngOnInit() {
    this.getComments();
  }

  getComments() {
    let url = this.router.url;

    if (url.includes('posts/')) {
      this.comments.blog_id = url.split("/")[2];
      this.commentsService.getCommentsByBlogID(this.comments.blog_id).subscribe((result: any) => {
        this.comments = result;
        console.log('result is ', result);
    })
      } else {
        alert('wrong url')
      }

  }
}
