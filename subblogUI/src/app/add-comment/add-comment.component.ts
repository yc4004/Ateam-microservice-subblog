import { Component } from '@angular/core';
import { CommentService } from './add-comment.service';
import { Comment } from '../models/comment.model';
import { Router } from '@angular/router';

@Component({
  selector: 'add-comment',
  templateUrl: './add-comment.component.html',
  styleUrls: ['./add-comment.component.css'],
  providers: [ CommentService ]
})
export class AddCommentComponent {

  public comment : Comment;

  constructor(private commentService: CommentService, private router: Router) {
       this.comment = new Comment();
  }

  addComment() {
    if (this.comment.blog_id && this.comment.content) {
      this.commentService.addComment(this.comment).subscribe(result =>{
        console.log('result is ', result);

      });
    } else {
      alert('blog_id and conmment required')
    }
  }

}
