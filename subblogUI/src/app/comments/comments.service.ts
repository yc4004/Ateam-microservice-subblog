import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Comment } from '../models/comment.model';

@Injectable()
export class CommentsService {
  private url = 'http://127.0.0.1:5011/posts';

  constructor(private http: HttpClient) {}

  getCommentsByBlogID(blog_id: string) {
    return this.http.get(this.url + '/' + blog_id);
  }
}
