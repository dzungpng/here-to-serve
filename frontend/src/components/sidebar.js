import React from 'react'
import Box from 'react-bulma-components/lib/components/box'
import { Link } from 'react-router-dom'

import Menu from 'react-bulma-components/lib/components/menu'
import CustomSections from './customSections'
import {
  PlusCircle,
  Calendar,
  AlertCircle,
  UserPlus,
  Users,
  Paperclip,
  Mail,
  Send,
  Inbox,
  Edit,
} from 'react-feather'

const SideBar = (props) => {
  return (
    <div>
      <CustomSections />
      <Menu color='white'>
        <Menu.List>
          <Box>
            <Link to='/create-new-activity'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <PlusCircle size={12} style={{ marginRight: '10px' }} />
                  <p>Create New Activity</p>
                </div>
              </p>
            </Link>

            <Link to='#'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <Calendar size={12} style={{ marginRight: '10px' }} />
                  <p>Manage Existing Activities</p>
                </div>
              </p>
            </Link>

            <Link to='/activity-report'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <Paperclip size={12} style={{ marginRight: '10px' }} />
                  <p>Activity Report</p>
                </div>
              </p>
            </Link>
            <hr />

            <Link to='/community-people'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <Users size={12} style={{ marginRight: '10px' }} />{' '}
                  <p>View & Update Member Information</p>
                </div>
              </p>
            </Link>

            <Link to='#'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <UserPlus size={12} style={{ marginRight: '10px' }} />
                  <p>Invite Added Members to Sign in</p>
                </div>
              </p>
            </Link>

            <Link to='#'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <AlertCircle size={12} style={{ marginRight: '10px' }} />
                  <p>Review Join Requests</p>
                </div>
              </p>
            </Link>

            <hr />

            <Link to='/announcements'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <Inbox size={12} style={{ marginRight: '10px' }} />{' '}
                  <p>Manage Announcements & Emails</p>
                </div>
              </p>
            </Link>

            <Link to='/create-announcement'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <Send size={12} style={{ marginRight: '10px' }} />{' '}
                  <p>Add Announcement</p>
                </div>
              </p>
            </Link>

            <Link to='#'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <Mail size={12} style={{ marginRight: '10px' }} />{' '}
                  <p>Email Members</p>
                </div>
              </p>
            </Link>

            <Link to='/edit-community'>
              <p className='sidebar'>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <Edit size={12} style={{ marginRight: '10px' }} />{' '}
                  <p>Edit Community Information</p>
                </div>
              </p>
            </Link>
          </Box>
        </Menu.List>
      </Menu>
    </div>
  )
}

export default SideBar
