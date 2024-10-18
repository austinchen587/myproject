import React from 'react';
import './EditAttendanceForm.css';  // 引入局部样式文件

const EditAttendanceForm = ({ customer, handleInputChange }) => (
  <div className="edit-attendance-form-container">
    
    {/* 是否到课提醒 */}
    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="is_course_reminder"
        checked={customer.is_course_reminder}
        onChange={handleInputChange}
      />
      <label className="form-check-label">是否到课提醒</label>
    </div>

    {/* 参加第一天直播 */}
    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="attended_first_live"
        checked={customer.attended_first_live}
        onChange={handleInputChange}
      />
      <label className="form-check-label">参加第一天直播</label>
    </div>

    {/* 第一日观看时长 */}
    <div className="form-group">
      <label>第一天观看时长 (分钟)</label>
      <input
        type="number"
        className="form-control custom-input"
        name="first_day_watch_duration"
        value={customer.first_day_watch_duration}
        onChange={handleInputChange}
        placeholder="请输入时长"
      />
    </div>

    {/* 参加第二天直播 */}
    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="attended_second_live"
        checked={customer.attended_second_live}
        onChange={handleInputChange}
      />
      <label className="form-check-label">参加第二天直播</label>
    </div>

    {/* 第二日观看时长 */}
    <div className="form-group">
      <label>第二天观看时长 (分钟)</label>
      <input
        type="number"
        className="form-control custom-input"
        name="second_day_watch_duration"
        value={customer.second_day_watch_duration}
        onChange={handleInputChange}
        placeholder="请输入时长"
      />
    </div>

    {/* 是否有马甲加学员 */}
    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="additional_students"
        checked={customer.additional_students}
        onChange={handleInputChange}
      />
      <label className="form-check-label">马甲加学员</label>
    </div>

    {/* 评论数 */}
    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="comments_count"
        checked={customer.comments_count}
        onChange={handleInputChange}
      />
      <label className="form-check-label">评论数</label>
    </div>

    {/* 是否进行人设聊天 */}
    <div className="form-check form-group">
      <input
        type="checkbox"
        className="form-check-input custom-checkbox"
        name="persona_chat"
        checked={customer.persona_chat}
        onChange={handleInputChange}
      />
      <label className="form-check-label">是否进行人设聊天</label>
    </div>

    {/* 第一天观后反馈 */}
    <div className="form-group">
      <label>第一天观后反馈</label>
      <select
        className="form-control custom-select"
        name="first_day_feedback"
        value={customer.first_day_feedback}
        onChange={handleInputChange}
      >
        <option value="满意">满意</option>
        <option value="一般">一般</option>
        <option value="不考虑">不考虑</option>
      </select>
    </div>

    {/* 第二天观后反馈 */}
    <div className="form-group">
      <label>第二天观后反馈</label>
      <select
        className="form-control custom-select"
        name="second_day_feedback"
        value={customer.second_day_feedback}
        onChange={handleInputChange}
      >
        <option value="满意">满意</option>
        <option value="一般">一般</option>
        <option value="不考虑">不考虑</option>
      </select>
    </div>

    {/* 客户描述 */}
    <div className="form-group">
      <label>客户描述</label>
      <textarea
        className="form-control custom-textarea"
        name="description"
        value={customer.description}
        onChange={handleInputChange}
        placeholder="请输入描述"
        rows="4"
      />
    </div>
  </div>
);

export default EditAttendanceForm;