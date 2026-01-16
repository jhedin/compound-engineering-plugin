# EARS Format Reference

EARS = Easy Approach to Requirements Syntax

A structured format for writing clear, testable requirements.

## User Story Format

```
As a [role], I want [feature], so that [benefit].
```

**Example:**
> As a registered user, I want to reset my password via email, so that I can regain access to my account if I forget my credentials.

## Acceptance Criteria Format

Each requirement includes numbered acceptance criteria using EARS keywords:

### EARS Keywords

| Keyword | Usage | Example |
|---------|-------|---------|
| **SHALL** | Mandatory requirement | The system SHALL hash passwords using bcrypt |
| **SHOULD** | Recommended but not mandatory | The system SHOULD display password strength |
| **MAY** | Optional feature | The system MAY offer social login |
| **WHEN** | Trigger condition | WHEN the user clicks "Submit" |
| **IF** | Conditional behavior | IF the email is invalid |
| **WHERE** | Context specification | WHERE the user has admin role |

### Criteria Patterns

**Ubiquitous (always true):**
```
The system SHALL [action].
```

**Event-driven:**
```
WHEN [trigger], the system SHALL [response].
```

**Conditional:**
```
IF [condition], THEN the system SHALL [response].
```

**State-driven:**
```
WHERE [state], the system SHALL [behavior].
```

**Complex:**
```
WHERE [state], WHEN [trigger], IF [condition], THEN the system SHALL [response].
```

## Complete Example

### 1. User Authentication

As a user, I want to log in with my email and password, so that I can access my account securely.

**Acceptance Criteria:**

1.1. WHEN the user enters valid credentials and clicks "Login", the system SHALL authenticate the user and redirect to the dashboard.

1.2. WHEN the user enters invalid credentials, the system SHALL display the error message "Invalid email or password" without specifying which field was incorrect.

1.3. IF the user fails 5 consecutive login attempts, THEN the system SHALL lock the account for 15 minutes and send a notification email.

1.4. The system SHALL hash all passwords using bcrypt with a cost factor of at least 12.

1.5. WHERE the user has enabled two-factor authentication, WHEN credentials are valid, the system SHALL prompt for the 2FA code before granting access.

### 2. Password Reset

As a user, I want to reset my password via email, so that I can regain access if I forget my credentials.

**Acceptance Criteria:**

2.1. WHEN the user requests a password reset, the system SHALL send a reset link to the registered email within 30 seconds.

2.2. The reset link SHALL expire after 1 hour.

2.3. WHEN the user clicks an expired link, the system SHALL display "This link has expired" and offer to send a new one.

2.4. The system SHALL invalidate all existing reset links when a new one is requested.

## Document Structure

A complete requirements document includes:

### 1. Introduction
Brief summary of the feature and its purpose.

### 2. User Stories
Hierarchical numbered list:
```
1. [Story Title]
   As a [role], I want [feature], so that [benefit].

   Acceptance Criteria:
   1.1. [criterion]
   1.2. [criterion]

2. [Story Title]
   ...
```

### 3. Non-Functional Requirements
- **Performance:** Response times, throughput, scalability
- **Security:** Authentication, authorization, data protection
- **Accessibility:** WCAG compliance, screen reader support
- **Reliability:** Uptime, error rates, recovery

### 4. Edge Cases
- Error scenarios and recovery
- Boundary conditions (empty, null, max values)
- Concurrent access handling
- Network failure behavior

### 5. Out of Scope
Explicit list of what this feature does NOT include. Prevents scope creep and sets clear boundaries.

## Tips for Good Requirements

1. **Be specific** - "fast" is vague, "under 200ms" is testable
2. **One requirement per criterion** - Don't combine multiple behaviors
3. **Use consistent terminology** - Define terms and use them consistently
4. **Make them testable** - Each criterion should have a clear pass/fail
5. **Avoid implementation details** - Focus on WHAT, not HOW
6. **Consider all user roles** - Admin, regular user, guest, etc.
7. **Include negative cases** - What should NOT happen
