import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import TypeWriter from '../TypeWriter.vue'

describe('TypeWriter', () => {
  it('renders properly', () => {
    const wrapper = mount(TypeWriter, { props: { msg: 'Hello Vitest' } })
    expect(wrapper.text()).toContain('Hello Vitest')
  })
})
