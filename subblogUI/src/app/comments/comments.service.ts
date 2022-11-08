import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Comment } from '../models/comment.model';
// import { CommentsService }

@Injectable()
export class CommentsService {
  private url = 'http://127.0.0.1:5011/posts';

  constructor(private http: HttpClient) {}

  getCommentsByBlogID(blog_id: string) {
    return this.http.get(this.url + '/' + blog_id);
  }

  private options = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
    body: {
      id: 1,
    },
  };

  deleteByID(id: any, blog_id: string) {
    return this.http.delete(this.url + '/' + blog_id, 
    {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
      body: {
        "id": id,
      },
    })
  }

}
