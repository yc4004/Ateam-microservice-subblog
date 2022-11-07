import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Comment } from '../models/comment.model';

@Injectable()
export class AddCommentService {

    private url = 'http://127.0.0.1:5011/posts'
 
    constructor(private http: HttpClient){
 
    }
     
    addComment(comment: Comment){
        return this.http.post(this.url + "/" + comment.blog_id + "/addcomment",{
            // blog_id : comment.blog_id,
            content : comment.content
        })
    }

}
