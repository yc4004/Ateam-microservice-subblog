import { Component } from '@angular/core';
import { AddCommentService } from './add-comment.service';
import { Comment } from '../models/comment.model';
import { Router } from '@angular/router';

@Component({
  selector: 'add-comment',
  templateUrl: './add-comment.component.html',
  styleUrls: ['./add-comment.component.css'],
  providers: [ AddCommentService ]
})
export class AddCommentComponent {

  public comment : Comment;

  constructor(private addcommentService: AddCommentService, 
              private router: Router) {
              this.comment = new Comment();
  }


  // get id from url, using: if (url.includes('posts/')) {url.split('') }
  addComment() {

    let url = this.router.url

    if (url.includes('posts/') && this.comment.content) {
      this.comment.blog_id = url.split("/")[2];
      this.addcommentService.addComment(this.comment).subscribe((result: any) => {this.comment = result;
        console.log('result is ', result);}
      );
      window.location.href = "/posts/" + this.comment.blog_id;
    } else {
      alert('conmment required')
    }

    // if (this.comment.blog_id && this.comment.content) {
    //   this.commentService.addComment(this.comment).subscribe(result =>{
    //     console.log('result is ', result);

    //   });
    // } else {
    //   alert('blog_id and conmment required')
    // }
  }
}
