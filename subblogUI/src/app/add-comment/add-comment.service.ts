import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Comment } from '../models/comment.model';

@Injectable()
export class CommentService {
 
    constructor(private http: HttpClient){
 
    }
     
    addComment(comment: Comment){
        return this.http.post('http://127.0.0.1:5011/comment',{
            blog_id : comment.blog_id,
            content : comment.content
        })
    }
 
}